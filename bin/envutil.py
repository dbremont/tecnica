#!/usr/bin/env python3
"""
Tiny stdlib .env loader. No python-dotenv dependency.

Reads <repo>/.env once, populates os.environ for keys that are not already
set (real environment variables win). Returns a small object with typed
accessors for the CouchDB connection settings used across bin/.
"""

import os
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
ENV_FILE = REPO / ".env"

_LOADED = False


def _load():
    global _LOADED
    if _LOADED:
        return
    _LOADED = True
    if not ENV_FILE.exists():
        return
    with open(ENV_FILE, "r", encoding="utf-8") as fh:
        for raw in fh:
            line = raw.strip()
            if not line or line.startswith("#") or "=" not in line:
                continue
            key, _, val = line.partition("=")
            key = key.strip()
            val = val.strip().strip('"').strip("'")
            os.environ.setdefault(key, val)


def _get(key, default=None):
    _load()
    return os.environ.get(key, default)


class CouchConfig:
    """Resolved CouchDB connection settings."""

    def __init__(self):
        self.url = (_get("COUCHDB_URL") or "http://127.0.0.1:5984").rstrip("/")
        self.db = _get("COUCHDB_DB") or "tecnica"
        self.user = _get("COUCHDB_USER")
        self.password = _get("COUCHDB_PASSWORD")

    @property
    def base(self):
        return self.url

    @property
    def db_url(self):
        return "%s/%s" % (self.url, self.db)

    def __repr__(self):
        return "CouchConfig(url=%r, db=%r, user=%r)" % (
            self.url,
            self.db,
            self.user,
        )


def couch():
    return CouchConfig()
