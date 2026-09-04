#!/usr/bin/env python3
"""
Sync server for the Tecnica Editor.

Serves the static app/ files and is the only frontend-facing surface:
the browser never talks to CouchDB directly.

  - GET  /api/health        -> pings CouchDB, reports db + doc count.
  - GET  /api/nodes         -> all graph nodes as a flat JSON array
                               (proxied from CouchDB; _id/_rev stripped,
                               the layout doc excluded).
  - GET  /api/layout        -> node positions {nodeId: [x, y]} from the
                               CouchDB 'layout' doc; falls back to the
                               static app/data/layout.json file. The source
                               is reported in the X-Layout-Source header.
  - POST /api/graph/save    -> upserts the patch {nodes, timestamp} into
                               CouchDB via _bulk_docs (server resolves _rev).

API paths under /app/api/... are treated as /api/... so the default dev
layout (--root ., pages under /app/) reaches the same endpoints as the
production layout (--root app).

CouchDB connection is read from .env (see bin/envutil.py). No file is written —
the old save-to-data.json code path has been removed; CouchDB is the backend.

Usage:

    python bin/sync.py
    python bin/sync.py --root . --port 8000

In the editor's Settings -> "Backend Sync" -> "Backend Save URL", enter:

    http://localhost:8000/api/graph/save
"""

import argparse
import json
import sys
from functools import partial
from http.server import HTTPServer, SimpleHTTPRequestHandler
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import couchdb_client  # noqa: E402
import envutil  # noqa: E402

SAVE_ENDPOINT = "/api/graph/save"
HEALTH_ENDPOINT = "/api/health"
NODES_ENDPOINT = "/api/nodes"
LAYOUT_ENDPOINT = "/api/layout"
LAYOUT_DOC_ID = "layout"
APP_PREFIX = "/app"


class SyncHandler(SimpleHTTPRequestHandler):
    """Serves static files and proxies all graph data to/from CouchDB."""

    def __init__(self, *args, layout_file=None, **kwargs):
        self.layout_file = Path(layout_file) if layout_file else None
        super().__init__(*args, **kwargs)

    # ------------------------------------------------------------------
    # CORS
    # ------------------------------------------------------------------

    def end_headers(self):
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header(
            "Access-Control-Allow-Methods",
            "GET, POST, OPTIONS",
        )
        self.send_header(
            "Access-Control-Allow-Headers",
            "Content-Type",
        )
        super().end_headers()

    def do_OPTIONS(self):
        self.send_response(204)
        self.end_headers()

    # ------------------------------------------------------------------
    # GET
    # ------------------------------------------------------------------

    def do_GET(self):
        path = self._api_path(self.path.split("?", 1)[0])

        if path == HEALTH_ENDPOINT:
            self._handle_health()
            return

        if path == NODES_ENDPOINT:
            self._handle_nodes()
            return

        if path == LAYOUT_ENDPOINT:
            self._handle_layout()
            return

        super().do_GET()

    def _api_path(self, path):
        """
        Map /app/api/... to /api/... so the default dev layout (--root .,
        pages under /app/) hits the same endpoints as --root app.
        """
        if path.startswith(APP_PREFIX + "/api/"):
            return path[len(APP_PREFIX):]
        return path

    def _handle_health(self):
        cfg = envutil.couch()
        client = couchdb_client.Client(cfg)

        couch_ok = False
        version = None
        try:
            status, body = client.get(cfg.url + "/")
            couch_ok = status == 200
            if isinstance(body, dict):
                version = body.get("version")
        except Exception as exc:
            version = "error: %s" % exc

        doc_count = None
        try:
            status, body = client.get(cfg.db_url)
            if status == 200 and isinstance(body, dict):
                doc_count = body.get("doc_count")
        except Exception:
            pass

        self._send_json(
            {
                "status": "ok" if couch_ok else "degraded",
                "service": "tecnica-sync",
                "couchdb_url": cfg.url,
                "couchdb_version": version,
                "couchdb_ok": couch_ok,
                "database": cfg.db,
                "doc_count": doc_count,
            }
        )

    def _handle_nodes(self):
        """
        Serve all graph nodes as a flat JSON array.

        Proxies CouchDB server-side (the browser never talks to it): every
        non-design doc, the 'layout' doc excluded, _id/_rev stripped — the
        same shape app/js/api.js consumes. Hard-fails with 502 when CouchDB
        is unreachable; there is deliberately no file fallback (the seed
        data.json is a snapshot, not the live store).
        """
        try:
            cfg = envutil.couch()
            docs = couchdb_client.all_docs(cfg)
        except Exception as exc:
            self._send_json(
                {
                    "status": "error",
                    "message": "CouchDB unavailable: %s" % exc,
                },
                502,
            )
            return

        nodes = []
        for doc in docs:
            if not isinstance(doc, dict):
                continue
            if doc.get("_id") == LAYOUT_DOC_ID or doc.get("type") == "layout":
                continue
            nodes.append(
                {k: v for k, v in doc.items() if k not in ("_id", "_rev")}
            )

        self._send_json(nodes)

    def _handle_layout(self):
        """
        Serve the precomputed graph layout.

        Primary source is the CouchDB doc _id "layout" (written by
        bin/layout.py). If that read fails or the doc is missing, fall back
        to the static layout file on disk. Responds with the bare positions
        map (same shape as layout.json); X-Layout-Source says which store
        was used.
        """
        # 1. Primary: the layout doc in CouchDB.
        try:
            cfg = envutil.couch()
            client = couchdb_client.Client(cfg)
            status, doc = client.get(cfg.db_url + "/" + LAYOUT_DOC_ID)
            positions = doc.get("positions") if (
                status == 200 and isinstance(doc, dict)
            ) else None
            if isinstance(positions, dict) and positions:
                self._send_json(positions, extra_headers={"X-Layout-Source": "db"})
                return
        except Exception:
            pass

        # 2. Fallback: the static layout file.
        try:
            payload = json.loads(self.layout_file.read_text(encoding="utf-8"))
            if isinstance(payload, dict) and payload:
                self._send_json(payload, extra_headers={"X-Layout-Source": "file"})
                return
        except Exception:
            pass

        self._send_json(
            {
                "status": "error",
                "message": "layout unavailable (CouchDB doc %r unreadable and %s missing; run python bin/layout.py)"
                % (LAYOUT_DOC_ID, self.layout_file),
            },
            404,
        )

    # ------------------------------------------------------------------
    # POST
    # ------------------------------------------------------------------

    def do_POST(self):
        path = self._api_path(self.path.split("?", 1)[0])

        if path == SAVE_ENDPOINT:
            self._handle_save()
        else:
            self.send_error(404, "Not Found")

    def _handle_save(self):
        try:
            length = int(self.headers.get("Content-Length", 0))
            raw = self.rfile.read(length) if length else b"{}"

            patch = json.loads(raw)
            changed = patch.get("nodes", [])

            if not changed:
                self._send_json({"status": "ok", "saved": 0})
                return

            result = couchdb_client.bulk_upsert(changed)

            self._send_json(
                {
                    "status": "ok",
                    "saved": result["ok"],
                    "new": result["new"],
                    "updated": result["updated"],
                    "errors": result["errors"],
                    "timestamp": patch.get("timestamp", ""),
                }
            )

        except couchdb_client.CouchError as exc:
            self._send_json(
                {
                    "status": "error",
                    "message": str(exc),
                },
                502,
            )

        except json.JSONDecodeError as exc:
            self._send_json(
                {
                    "status": "error",
                    "message": "Invalid JSON: %s" % exc,
                },
                400,
            )

        except Exception as exc:
            self._send_json(
                {
                    "status": "error",
                    "message": str(exc),
                },
                500,
            )

    # ------------------------------------------------------------------
    # Helpers
    # ------------------------------------------------------------------

    def _send_json(self, obj, code=200, extra_headers=None):
        body = json.dumps(obj).encode("utf-8")

        self.send_response(code)
        self.send_header(
            "Content-Type",
            "application/json",
        )
        self.send_header(
            "Content-Length",
            str(len(body)),
        )
        for key, value in (extra_headers or {}).items():
            self.send_header(key, value)
        self.end_headers()

        self.wfile.write(body)

    def log_message(self, fmt, *args):
        sys.stderr.write(
            "[sync] %s - %s\n" % (self.address_string(), fmt % args)
        )


def _couchdb_ready(cfg):
    """Preflight: refuse to start unless CouchDB and the database are reachable."""
    client = couchdb_client.Client(cfg)

    try:
        status, body = client.get(cfg.url + "/")
    except Exception as exc:
        print(
            "[fatal] CouchDB unreachable at %s: %s" % (cfg.url, exc),
            file=sys.stderr,
        )
        return False

    if status != 200:
        print(
            "[fatal] CouchDB at %s returned HTTP %s" % (cfg.url, status),
            file=sys.stderr,
        )
        return False

    version = body.get("version") if isinstance(body, dict) else None
    print("[ok] CouchDB reachable: %s (version %s)" % (cfg.url, version))

    try:
        status, body = client.get(cfg.db_url)
    except Exception as exc:
        print(
            "[fatal] Cannot check database '%s' on %s: %s" % (cfg.db, cfg.url, exc),
            file=sys.stderr,
        )
        return False

    if status == 404:
        print(
            "[fatal] Database '%s' not found on %s"
            " (create it: curl -u <user>:<pass> -X PUT %s/%s — see README)"
            % (cfg.db, cfg.url, cfg.url, cfg.db),
            file=sys.stderr,
        )
        return False

    if status != 200:
        print(
            "[fatal] Database '%s' check returned HTTP %s" % (cfg.db, status),
            file=sys.stderr,
        )
        return False

    doc_count = body.get("doc_count") if isinstance(body, dict) else None
    print("[ok] Database ready: %s (doc_count=%s)" % (cfg.db, doc_count))
    return True


def main():
    parser = argparse.ArgumentParser(
        prog="sync.py",
        description="Tecnica sync server (static + CouchDB proxy).",
    )

    here = Path(__file__).resolve().parent
    repo = here.parent

    parser.add_argument(
        "--root",
        default=str(repo),
        help="Directory to serve static files from (default: repo root).",
    )

    parser.add_argument(
        "-p",
        "--port",
        type=int,
        default=8000,
        help="Port to listen on (default: 8000).",
    )

    parser.add_argument(
        "--host",
        default="0.0.0.0",
        help="Host/interface to bind (default: 0.0.0.0).",
    )

    parser.add_argument(
        "--layout-file",
        default=str(repo / "app" / "data" / "layout.json"),
        help="Static layout file used when the CouchDB layout doc is"
             " unavailable (default: app/data/layout.json).",
    )

    args = parser.parse_args()

    root_dir = Path(args.root).resolve()

    if not root_dir.exists():
        print(
            "ERROR: static root not found: %s" % root_dir,
            file=sys.stderr,
        )
        return 1

    cfg = envutil.couch()

    if not _couchdb_ready(cfg):
        print(
            "[fatal] Startup aborted: CouchDB backend is required.",
            file=sys.stderr,
        )
        return 1

    handler = partial(
        SyncHandler,
        directory=str(root_dir),
        layout_file=args.layout_file,
    )

    server = HTTPServer(
        (args.host, args.port),
        handler,
    )

    display_host = (
        "localhost"
        if args.host in ("0.0.0.0", "::")
        else args.host
    )

    print("══════════════════════════════════════════════")
    print("  Tecnica Sync Server (CouchDB backend)")
    print("──────────────────────────────────────────────")
    print("  Root:    %s" % root_dir)
    print("  CouchDB: %s/%s" % (cfg.url, cfg.db))
    print(
        "  Save:    http://%s:%d%s" % (display_host, args.port, SAVE_ENDPOINT)
    )
    print(
        "  Nodes:   http://%s:%d%s" % (display_host, args.port, NODES_ENDPOINT)
    )
    print(
        "  Layout:  http://%s:%d%s" % (display_host, args.port, LAYOUT_ENDPOINT)
    )
    print(
        "  Health:  http://%s:%d%s" % (display_host, args.port, HEALTH_ENDPOINT)
    )
    print("══════════════════════════════════════════════")
    print()

    try:
        server.serve_forever()

    except KeyboardInterrupt:
        print("\nShutting down...")
        server.shutdown()


if __name__ == "__main__":
    raise SystemExit(main())
