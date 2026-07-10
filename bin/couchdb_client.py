#!/usr/bin/env python3
"""
Shared stdlib CouchDB client for the bin/ scripts.

Wraps urllib with Basic auth from bin/envutil.py. Returns (status, parsed_body)
so callers decide what to do with non-2xx. Also offers helpers for the common
Tecnica pattern: fetch all node docs, and bulk upsert node records by id.
"""

import base64
import json
import urllib.error
import urllib.request

import envutil


class CouchError(Exception):
    def __init__(self, status, body):
        self.status = status
        self.body = body
        super().__init__("CouchDB HTTP %s: %s" % (status, body))


class Client:
    def __init__(self, cfg=None):
        self.cfg = cfg or envutil.couch()

    def _headers(self):
        h = {"Accept": "application/json"}
        if self.cfg.user:
            token = base64.b64encode(
                ("%s:%s" % (self.cfg.user, self.cfg.password or "")).encode("utf-8")
            ).decode("ascii")
            h["Authorization"] = "Basic %s" % token
        return h

    def request(self, method, url, body=None):
        data = None
        headers = self._headers()
        if body is not None:
            data = json.dumps(body).encode("utf-8")
            headers["Content-Type"] = "application/json"
        req = urllib.request.Request(url, data=data, method=method, headers=headers)
        try:
            with urllib.request.urlopen(req, timeout=30) as resp:
                raw = resp.read()
                return resp.status, (json.loads(raw) if raw else None)
        except urllib.error.HTTPError as exc:
            raw = exc.read()
            try:
                parsed = json.loads(raw) if raw else None
            except ValueError:
                parsed = raw.decode("utf-8", "replace")
            return exc.code, parsed

    def get(self, url):
        return self.request("GET", url)

    def put(self, url, body=None):
        return self.request("PUT", url, body)

    def post(self, url, body):
        return self.request("POST", url, body)


def all_docs(cfg=None, keys=None):
    """All non-design docs as a list. Each doc keeps its _id/_rev."""
    c = Client(cfg)
    base = c.cfg.db_url + "/_all_docs?include_docs=true"
    if keys:
        status, body = c.post(base, {"keys": list(keys)})
    else:
        status, body = c.get(base)
    if status != 200:
        raise CouchError(status, body)
    docs = []
    for row in body.get("rows", []):
        doc = row.get("doc")
        if doc and not str(doc.get("_id", "")).startswith("_design"):
            docs.append(doc)
    return docs


def bulk_upsert(nodes, cfg=None):
    """
    Upsert a list of node dicts by id.

    - node["_id"] is forced to node["id"] (falls back to a generated id).
    - Existing _rev is fetched so updates do not 409.
    - Returns a dict summary: {ok, errors, new, updated}.
    """
    c = Client(cfg)
    prepared = []
    seen_ids = []
    for n in nodes:
        if not isinstance(n, dict):
            continue
        nid = n.get("id") or n.get("_id")
        if not nid:
            continue
        doc = dict(n)
        doc["_id"] = nid
        prepared.append(doc)
        seen_ids.append(nid)

    if not prepared:
        return {"ok": 0, "errors": [], "new": 0, "updated": 0}

    # Resolve current _revs for idempotent updates.
    status, body = c.post(
        c.cfg.db_url + "/_all_docs?include_docs=true", {"keys": seen_ids}
    )
    if status != 200:
        raise CouchError(status, body)
    rev_by_id = {}
    for row in body.get("rows", []):
        doc = row.get("doc")
        if isinstance(doc, dict) and doc.get("_rev"):
            rev_by_id[doc.get("_id")] = doc["_rev"]

    new = 0
    for doc in prepared:
        existing = rev_by_id.get(doc["_id"])
        if existing:
            doc["_rev"] = existing
            updated_flag = True
        else:
            doc.pop("_rev", None)
            updated_flag = False
        doc["_u"] = updated_flag  # transient; stripped before send

    payload = [{k: v for k, v in doc.items() if k != "_u"} for doc in prepared]
    status, body = c.post(c.cfg.db_url + "/_bulk_docs", {"docs": payload})
    if status not in (201, 202):
        raise CouchError(status, body)

    new = sum(1 for doc in prepared if not doc["_u"])
    updated = len(prepared) - new
    errors = [r for r in (body or []) if isinstance(r, dict) and not r.get("ok")]
    return {"ok": len(prepared) - len(errors), "errors": errors, "new": new, "updated": updated}
