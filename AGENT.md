# AGENT.md — notes for coding agents working in this repo

## What this is

Tecnica — a framework for rendering purposeful (agentic) operation: an ontology of
~40 technical-objects-as-graph-nodes, rendered as a WebGL (deck.gl) graph with a
read-only viewer (`app/graph.html`) and an editor (`app/edit.html`). No Node build
step, no test suite; Python stdlib backend scripts in `bin/`.

## Architecture contract (do not break)

**The browser never talks to CouchDB.** `bin/sync.py` is the only frontend-facing
surface (static files + same-origin API). CORS on CouchDB must stay disabled.

- Frontend data access: `app/js/api.js` (`window.Api`: `loadNodes()` → `api/nodes`,
  `loadLayout()` → `api/layout`, fallback `data/layout.json`). There is no couch.js.
- `bin/sync.py` endpoints: `GET /api/health`, `GET /api/nodes` (proxies CouchDB,
  strips `_id`/`_rev`, excludes the `layout` doc; hard 502, no file fallback),
  `GET /api/layout`, `POST /api/graph/save`.
- Node docs: CouchDB db `tecnica`, `_id == node.id`; layout lives in doc `_id: "layout"`.
  `app/data/data.json` is the seed snapshot only — never the live store, never fetched
  by the frontend.
- Path quirk: API paths under `/app/api/...` are normalized to `/api/...` so dev
  (`python bin/sync.py` with default `--root .`, pages at `/app/graph.html`) and prod
  (container runs `--root app`) behave the same. Relative `api/...` fetches in JS.

## Run / verify locally

```
python bin/sync.py                 # serves repo root on :8000, needs CouchDB up
python bin/seed_couchdb.py         # seed data.json -> CouchDB (idempotent)
python bin/layout.py               # recompute layout -> CouchDB layout doc + layout.json
```

CouchDB config comes from gitignored `.env`: `COUCHDB_URL`, `COUCHDB_DB`,
`COUCHDB_USER`, `COUCHDB_PASSWORD` (there is no `.env.example` yet, despite README).

Fresh CouchDB bootstrap (manual, two curls — see README "Data backend").

Verification (no test suite exists):
- `python -m py_compile bin/*.py`
- `node --check app/js/api.js`
- `curl :8000/api/nodes` → JSON array, no `_id`/`_rev`, no `layout` doc
- Headless smoke: `google-chrome --headless=new --no-sandbox --virtual-time-budget=8000 --dump-dom http://localhost:8000/edit.html` (check stderr for Uncaught errors)

## Git — gotchas (this will block your first commit)

- A pre-commit hook (`00-authorization-policy.sh`) requires every staged file to be
  explicitly marked first:
  `mark-for-commit <file>...` (sets xattr `user.checkin`; marks are cleaned after commit).
  Deletions don't need marking.
- A commit-msg hook **rewrites the message** to `type(main): message` — all repo
  history looks like that; don't fight it.
- Remote may be ahead of local (docs get pushed from elsewhere) — `git fetch` and
  rebase before pushing.
- `AGENT.md` is tracked; keep it current when you learn something durable about
  this repo.

## Deploy

Push to `main` → CI (`.github/workflows/deploy.yml`) builds and pushes
`ghcr.io/dbremont/tecnica:latest`. Then on the server run `./deploy.sh`
(pulls image, recreates `tecnica` container: `--network host`, port 8000,
`.env` mounted read-only).

- Don't deploy before CI publishes: detect the new image by comparing
  `docker manifest inspect -v ghcr.io/dbremont/tecnica:latest` digests before/after.
- Container crash-looping with `OSError: [Errno 98] Address already in use` means
  another container took port 8000 (`docker ps -a`, look for port mappings) —
  `docker logs tecnica` confirms. Stray containers have appeared here before.
- `gh` CLI is not installed; use the public GitHub API or registry digests.

## Tooling notes

- `rg` may fail with "JSON record exceeded 65536 bytes" on the huge single-file HTML
  pages (edit.html is ~8k lines, graph.html ~3.6k); scope the include pattern or use
  `bash` + `rg` directly.
- Everything is stdlib Python 3.12 + vanilla JS + vendored deck.gl
  (`app/vendor/deck.min.js`); do not introduce package managers or build steps.
- User-facing pages must not reference backend scripts (`bin/...`, `python ...`) in
  UI strings — backend hints live in docs (README/spec) and server logs only.
