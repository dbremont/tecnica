# Tecnica — Spec

> **Status legend:** ✅ built & in this repo · 🎯 target / not yet implemented

- **Schema:** `app/data/schema/schema.json` ✅ — JSON Schema (draft 2020-12). Defines one "node"
  object: 20 required fields, a 6-value `layer` enum, a ~40-value `category` enum, a per-node
  `relationship_set` edge list (13 relation families, 45 relation types), and 39 per-category
  conditional subschemas that bind `particular_characterization` to a `<Category>Specific` def.
  `additionalProperties: false` throughout.
- **Design rationale:** `app/data/schema/note` ✅ — Markdown. The prose source of the ontology:
  category catalogue, field meanings, edge families, and the 6 layers. Read this to understand
  *why* the schema is shaped the way it is.
- **Data:** stored in **CouchDB** (the `tecnica` DB; one document per node, `_id = node["id"]`).
  `app/data/data.json` is the **seed source** (`python bin/seed_couchdb.py`) and stays in-repo — it
  is not the live store. Nodes carry **no spatial fields** (no `x`/`y`); edges embed per-node inside
  `relationship_set`, not as a separate edge list.

## Rendering & Data Pipeline

The graph is served as three self-contained HTML pages under `app/`. **The renderer has migrated
from Canvas2D + a live force simulation to a precomputed-layout + deck.gl (WebGL) pipeline.** Both
the viewer and the editor are migrated.

| File | Role | Renderer | Persists? |
|------|------|----------|-----------|
| `app/index.html` ✅ | Landing / overview | Decorative ambient Canvas2D only (random particles, unrelated to `data.json`) | No |
| `app/graph.html` ✅ | Read-only interactive viewer | **deck.gl (WebGL) + precomputed layout** | No |
| `app/edit.html` ✅ | Editor / authoring surface | **deck.gl (WebGL) + precomputed layout** | Yes (patch POST or JSON download) |

The pipeline has three pillars:

1. **Precompute (Python).** ✅ `bin/layout.py` writes `app/data/layout.json` = `{ "<id>": [x, y] }`.
   Run manually; no live force simulation at render time.
2. **GPU renderer (deck.gl).** ✅ for the viewer, 🎯 for the editor. A vendored, offline deck.gl
   bundle draws nodes/edges/labels; GPU picking replaces O(N) hit-testing; GPU-side visibility
   filtering scales to 100k+ nodes.
3. **Shared renderer module.** ✅ `app/vendor/socio-graph.js` (`window.SocioGraph`) holds the deck
   glue so both pages render identically.

### Precompute — `bin/layout.py` ✅

Pure-Python, stdlib only. Reads nodes from **CouchDB** by default (`--source couch`; override with
`--source file --data-file ...`), writes `layout.json`:

```
python bin/layout.py
python bin/layout.py --source file --data-file app/data/data.json --layout-file app/data/layout.json --spacing 80 --iterations 300
```

Algorithm: union-find connected components from `relationship_set` → **sunflower (phyllotaxis)
packing for isolated nodes** (the majority) + **per-component Fruchterman–Reingold** for the small
connected clusters, packed in an outer phyllotaxis ring around the isolate field. Deterministic
(seeded) and linear in N. Current dataset: 40 nodes (6 isolated, 6 clusters) in ~100 ms.

**Recompute is manual for now** 🎯 — there is no `/api/layout/recompute` endpoint yet (`bin/sync.py`
exposes `/api/graph/save`, now proxied to CouchDB, and `/api/health`). After editing data, re-run the script and reload.

**Missing-position fallback** ✅: if a node exists in CouchDB but not in `layout.json` (e.g. a
node added since the last recompute), `SocioGraph.seedPositions()` places it randomly within the
current layout bounds rather than at the origin.

### Vendored renderer — `app/vendor/` ✅

- `deck.min.js` (~1.5 MB) — the official deck.gl@9.1.12 standalone bundle
  (`https://unpkg.com/deck.gl@9.1.12/dist.min.js`), committed. Exposes global `deck` with `Deck`,
  `OrthographicView`, `ScatterplotLayer`, `LineLayer`, `TextLayer`, `DataFilterExtension`. **No Node,
  no build step, no runtime CDN** — loaded with a plain `<script>` tag. (Larger than the ~660 KB
  trimmed esbuild bundle the original plan envisaged, but that would require a Node build, which the
  project deliberately avoids.)
- `socio-graph.js` (`window.SocioGraph`) — pure functions: `createDeck` (a `Deck` + `OrthographicView`
  with `controller:false, flipY:true`), `camToViewState` (the host's `cam={x,y,z}` → deck
  `viewState`), `buildLayers` (edges `LineLayer`, nodes `ScatterplotLayer`, highlight rings,
  `TextLayer` labels), `pickAt` (O(1) GPU pick via `deck.pickObject`), `seedPositions`, `fitCam`.

> **Camera contract.** The host owns `cam = {x, y, z}` with the Canvas2D-style transform
> `screen = world*cam.z + {cam.x, cam.y}` (y-down). `camToViewState` converts this to deck's
> `{target, zoom}` with `flipY:true` so the WebGL view is pixel-identical to the legacy camera —
> verified by a headless pick test (a node whose math screen-y is 300 is hit at y=300, not mirrored).

**Scale design (target 100k+).** Positions are static (no per-frame sim). `DataFilterExtension`
keeps the full dataset on the GPU and shows/hides nodes+edges by filter without rebuilding arrays.
Picking is one `ReadPixels` (O(1)). Labels are LOD'd by zoom + degree so we never draw 100k texts.
Layers rebuild only on state change (`dirty` flag) or zoom band change; the view matrix alone is
pushed every frame.

### Viewer — `app/graph.html` ✅ (deck.gl)

Loads nodes from **CouchDB** (via `app/js/couch.js`) **and** `layout.json` together (`Promise.all`), seeds positions via
`SocioGraph.seedPositions`, creates the deck instance, and drives it from `cam`. The render loop
(`render()`): advance the camera tween → rebuild layers only if `dirty` or zoom band changed → push
`viewState` → redraw the (Canvas2D) minimap. Preserved from the Canvas2D version: `cam` pan/zoom/fit,
category/layer/time/family filters (→ `DataFilterExtension`), search + dropdown, the HTML inspect
panel, the HTML tooltip, the minimap, and keybindings (F=fit, E=epistemic, S=sidebar, /=search,
?=help, Esc). **Removed** for this migration: the Force↔UMAP projection toggle and the six Canvas2D
"visual lenses" (hulls/heatmap/centrality/confidence/flow/observability). Picking is `SocioGraph.pickAt`.

### Editor — `app/edit.html` ✅ (deck.gl)

Migrated to the same `SocioGraph` module as the viewer. It loads nodes from **CouchDB** + `layout.json`, seeds
positions, creates the deck instance, and drives it from `cam`. The render loop (`animate()`):
advance the camera tween → rebuild layers only if `dirty` or zoom band changed → push `viewState` →
redraw the (Canvas2D) minimap. **Every editor behavior is preserved**: click-to-select (opens the
form panel), node drag, link-mode (plum source ring + rubber-band line to the cursor, click a target
to create an edge), add node, delete, search highlights (cyan rings), and save (partial patch POST
`{nodes, timestamp}` to an opt-in `saveUrl`, else JSON download). `hitTest` now delegates to
`SocioGraph.pickAt` (O(1) GPU pick). Editor-only layers added to `socio-graph.js`: stackable highlight
rings (selected/search/link-source/hover) and the link rubber-band `LineLayer`. New nodes seed a
fallback position and are picked up by the next manual `python bin/layout.py`. The old Canvas2D
`draw()` / `simulate()` / silhouette code remains in the file as dead code.

### Scalability

Both pages: no live simulation, O(1) GPU picking, GPU-side filtering (`DataFilterExtension`) → the
architecture scales toward the 100k+ target. (Layer rebuilds are gated by a `dirty` flag and zoom-band
changes, so idle frames only push the view matrix; a future optimization for true 100k *drag* fidelity
is typed-array position attributes + per-node `updateTriggers` instead of full layer rebuilds.)

### Data + layout contract

Both pages require both files present:

| Source | Purpose | Origin |
|--------|---------|--------|
| **CouchDB `tecnica`** ✅ | Node/edge content (the schema above); one doc per node. | Authored / edited; seeded from `app/data/data.json`. |
| `app/data/data.json` ✅ | Seed source for CouchDB. | `python bin/seed_couchdb.py` |
| `app/data/layout.json` ✅ | Precomputed `[x, y]` per node id. | `python bin/layout.py` |

If CouchDB is unreachable/empty the page shows an actionable loader error (editor: minimal fallback
graph). If `layout.json` is missing it falls back to random placement (with a console warning) so the
page still renders.

### Notes
- Positions are ephemeral in CouchDB, so `layout.json` is additive — the data format is unchanged.
- The `cam` model maps onto deck's `OrthographicView` viewState (`flipY:true` to match the y-down
  camera — verified by a headless pick test).
- Recompute is still manual (`python bin/layout.py`); a `/api/layout/recompute` endpoint is a future
  convenience.
- `bin/sync.py` no longer reads/writes `data.json`: it serves static files and proxies
  `/api/graph/save` to CouchDB (CouchDB connection from `.env` via `bin/envutil.py`).
