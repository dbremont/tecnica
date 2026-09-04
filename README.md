# Tecnica

> A **framework for rendering**  purposeful (agentic) operation intelligible.

> We know there are **techniques for describing reality**, but these are techniques for describing, structuring, and operationalizing purposeful action within reality.

## Working On

- How to take 'Bremontix Ars' and extract - the concepts and add them to our dataset.

- (Projections) PCA or UMAP Embedding:  Treat each node as a vector of features (confidence, degree, inheritance level, observability (categorical), and even one‑hot encoded categories). Then reduce to 2D using PCA, t‑SNE, or UMAP.

## Data backend

The data backend is **CouchDB** (the `tecnica` database). Connection is configured
in a gitignored `.env` (see `.env.example`).

- Bootstrap CouchDB once (fresh install; adapt host/port to `COUCHDB_URL`/`COUCHDB_DB` in `.env`, add `-u user:pass` when the admin party is disabled):

  ```
  curl -X PUT http://127.0.0.1:5984/tecnica
  curl -X PUT http://127.0.0.1:5984/tecnica/_security -H 'Content-Type: application/json' -d '{}'
  ```

  The first creates the `tecnica` DB, the second clears `_security` so the sync server can read anonymously. CORS must stay disabled (the CouchDB default) so the browser can never reach the DB directly.
- `python bin/seed_couchdb.py` — seed `app/data/data.json` into CouchDB (idempotent; `data.json` is the seed source, not the live store).
- `python bin/sync.py` — static server + API: the only frontend-facing surface (the browser never talks to CouchDB directly, `app/js/api.js` hits these endpoints). `GET /api/nodes` serves the node array from CouchDB (`_id`/`_rev` stripped); the editor POSTs `/api/graph/save`, which upserts to CouchDB (`_bulk_docs`); `GET /api/layout` serves the precomputed layout from the CouchDB `layout` doc with `app/data/layout.json` as fallback (`X-Layout-Source` header reports the source).
- `python bin/layout.py` — precomputes the node layout and stores it in **both** the CouchDB `layout` doc (primary) and `app/data/layout.json` (fallback); reads nodes from CouchDB by default (`--source couch`; `--no-db` writes the file only).

## Deployment

CI (`.github/workflows/deploy.yml`) builds the image on every push to `main`
and pushes it to GHCR as `ghcr.io/dbremont/tecnica:latest`.

On the server, `./deploy.sh` pulls the latest image and (re)spawns the
container:

- Port: the container runs with `--network host` and serves directly on
  `TECNICA_PORT` (default `8000`).
- CouchDB config: the repo's `.env` is mounted read-only into the container
  at `/srv/.env`, where `bin/envutil.py` reads it. Real environment
  variables override `.env` values.
- With host networking, `COUCHDB_URL=http://127.0.0.1:5984` in `.env` works
  as-is — the container shares the host's network stack.

## TODO

- [x] Save things to the database - and implement the server mechanism similar to autoregia.
- [x] Pre-compute the layout.json (stored in the CouchDB `layout` doc, served via `GET /api/layout`, file as fallback)

## References

- [Philosophia Artium Technicarum et Operis](https://www.notion.so/Philosophia-Artium-Technicarum-et-Operis-355c0f5171ec808b82f8d7a85e8134cd?source=copy_link)
