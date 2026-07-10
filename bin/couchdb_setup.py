#!/usr/bin/env python3
"""
One-time CouchDB setup for Tecnica.

  - Enables CORS so the browser can read/write CouchDB directly.
  - Creates the target database if it does not exist.

Idempotent: safe to re-run. Uses only the stdlib + bin/envutil.py for config.

    python bin/couchdb_setup.py
"""

import json
import sys
import urllib.error
import urllib.request
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import envutil  # noqa: E402

# CORS knobs (CouchDB _config values are JSON strings).
CORS_CONFIG = {
    "httpd/enable_cors": "true",
    "cors/origins": "*",
    "cors/credentials": "false",
    "cors/headers": "accept, authorization, content-type, origin, referer",
    "cors/methods": "GET, PUT, POST, HEAD, DELETE",
}


def _req(method, url, cfg, body=None):
    data = None
    headers = {"Accept": "application/json"}
    if body is not None:
        data = json.dumps(body).encode("utf-8")
        headers["Content-Type"] = "application/json"
    if cfg.user:
        import base64

        token = base64.b64encode(
            ("%s:%s" % (cfg.user, cfg.password or "")).encode("utf-8")
        ).decode("ascii")
        headers["Authorization"] = "Basic %s" % token
    req = urllib.request.Request(url, data=data, method=method, headers=headers)
    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            raw = resp.read()
            return resp.status, (json.loads(raw) if raw else None)
    except urllib.error.HTTPError as exc:
        raw = exc.read()
        try:
            parsed = json.loads(raw) if raw else None
        except ValueError:
            parsed = raw.decode("utf-8", "replace")
        return exc.code, parsed


def main():
    cfg = envutil.couch()
    print("CouchDB: %s  db=%s  user=%s" % (cfg.url, cfg.db, cfg.user))

    # 1. CORS config via the local node.
    for key, val in CORS_CONFIG.items():
        url = "%s/_node/_local/_config/%s" % (cfg.url, key)
        code, body = _req("PUT", url, cfg, body=val)
        ok = code in (200, 201, 202, 204)
        print("  cors %-22s -> %s %s" % (key, code, "" if ok else body))
        if not ok:
            print("ERROR: could not set %s" % key, file=sys.stderr)
            return 1

    # 2. Create the database if missing (412 = already exists).
    code, body = _req("PUT", cfg.db_url, cfg)
    if code in (201, 202):
        print("  db created: %s" % cfg.db)
    elif code == 412:
        print("  db exists:  %s" % cfg.db)
    else:
        print("ERROR: db create failed: %s %s" % (code, body), file=sys.stderr)
        return 1

    # 3. Empty _security so the browser can read anonymously (this install
    #    defaults new DBs to _admin-only members, which blocks anon reads).
    code, body = _req("PUT", cfg.db_url + "/_security", cfg, body={})
    if code in (200, 201, 202):
        print("  db _security cleared (public reads)")
    else:
        print("  WARN: could not clear _security: %s %s" % (code, body))

    print("CouchDB ready.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
