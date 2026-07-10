#!/usr/bin/env python3
"""
Seed CouchDB from app/data/data.json.

Each node becomes a CouchDB document with _id == node["id"]. Idempotent:
re-running updates existing docs (current _rev is resolved first) and inserts
missing ones. data.json stays in place as the seed source — it is NOT deleted.

    python bin/seed_couchdb.py
    python bin/seed_couchdb.py --data-file app/data/data.json
"""

import argparse
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import couchdb_client  # noqa: E402
import envutil  # noqa: E402


def main(argv=None):
    p = argparse.ArgumentParser(prog="seed_couchdb.py")
    here = Path(__file__).resolve().parent
    repo = here.parent
    p.add_argument(
        "--data-file", default=str(repo / "app" / "data" / "data.json")
    )
    args = p.parse_args(argv)

    data_path = Path(args.data_file)
    if not data_path.exists():
        print("ERROR: data file not found: %s" % data_path, file=sys.stderr)
        return 1

    cfg = envutil.couch()
    print("Seeding %s -> %s/%s" % (data_path, cfg.url, cfg.db))

    with open(data_path, "r", encoding="utf-8") as fh:
        raw = json.load(fh)
    arr = raw if isinstance(raw, list) else raw.get("nodes", raw.get("categories", []))

    nodes = [n for n in arr if isinstance(n, dict) and (n.get("id") or n.get("_id"))]
    if not nodes:
        print("ERROR: no node records with an id in %s" % data_path, file=sys.stderr)
        return 1

    result = couchdb_client.bulk_upsert(nodes, cfg)
    print(
        "Seeded: %d ok (%d new, %d updated), %d errors."
        % (result["ok"], result["new"], result["updated"], len(result["errors"]))
    )
    for err in result["errors"][:10]:
        print("  ! %s" % err, file=sys.stderr)
    return 0 if not result["errors"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
