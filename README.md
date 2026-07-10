# Tecnica

> A **framework for rendering**  purposeful (agentic) operation intelligible.

> We know there are **techniques for describing reality**, but these are techniques for describing, structuring, and operationalizing purposeful action within reality.

## Working On

- How to take 'Bremontix Ars' and extract - the concepts and add them to our dataset.

- (Projections) PCA or UMAP Embedding:  Treat each node as a vector of features (confidence, degree, inheritance level, observability (categorical), and even one‑hot encoded categories). Then reduce to 2D using PCA, t‑SNE, or UMAP.

## Data backend

The data backend is **CouchDB** (the `tecnica` database). Connection is configured
in a gitignored `.env` (see `.env.example`).

- `python bin/couchdb_setup.py` — enable CORS, create the `tecnica` DB with public reads.
- `python bin/seed_couchdb.py` — seed `app/data/data.json` into CouchDB (idempotent; `data.json` is the seed source, not the live store).
- `python bin/sync.py` — static server + write proxy: the editor POSTs `/api/graph/save`, which upserts to CouchDB (`_bulk_docs`). Reads go straight from the browser to CouchDB via `app/js/couch.js`.
- `python bin/layout.py` — precomputes `app/data/layout.json`, reading nodes from CouchDB by default (`--source couch`).

## TODO

- [x] Save things to the database - and implement the server mechanism similar to autoregia.
- [ ] Pre-compute the layout.json

## References

- [Philosophia Artium Technicarum et Operis](https://www.notion.so/Philosophia-Artium-Technicarum-et-Operis-355c0f5171ec808b82f8d7a85e8134cd?source=copy_link)
