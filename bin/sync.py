#!/usr/bin/env python3
"""
Sync server for the Tecnica Editor.

Serves the static app/ files and proxies graph saves to CouchDB.

  - GET  /api/health        -> pings CouchDB, reports db + doc count.
  - POST /api/graph/save    -> upserts the patch {nodes, timestamp} into
                               CouchDB via _bulk_docs (server resolves _rev).

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


class SyncHandler(SimpleHTTPRequestHandler):
    """Serves static files and proxies graph save requests to CouchDB."""

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
        path = self.path.split("?", 1)[0]

        if path == HEALTH_ENDPOINT:
            self._handle_health()
            return

        super().do_GET()

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

    # ------------------------------------------------------------------
    # POST
    # ------------------------------------------------------------------

    def do_POST(self):
        path = self.path.split("?", 1)[0]

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

    def _send_json(self, obj, code=200):
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
        self.end_headers()

        self.wfile.write(body)

    def log_message(self, fmt, *args):
        sys.stderr.write(
            "[sync] %s - %s\n" % (self.address_string(), fmt % args)
        )


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

    args = parser.parse_args()

    root_dir = Path(args.root).resolve()

    if not root_dir.exists():
        print(
            "ERROR: static root not found: %s" % root_dir,
            file=sys.stderr,
        )
        return 1

    cfg = envutil.couch()

    handler = partial(
        SyncHandler,
        directory=str(root_dir),
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
