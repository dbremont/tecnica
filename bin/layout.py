#!/usr/bin/env python3
"""
Precompute a static graph layout for the Tecnica renderer.

Why this exists
---------------
The renderer (deck.gl) reads positions once at load and never runs a live
force simulation (that does not scale beyond a few thousand nodes). This tool
is the *only* thing that decides where nodes sit. Run it whenever data.json
changes:

    python bin/layout.py
    python bin/layout.py --data-file app/data/data.json --layout-file app/data/layout.json

Algorithm
---------
- Build an undirected graph from each node's `relationship_set` (edge only when
  both endpoints exist).
- Find connected components via union-find.
- Isolated nodes (component size 1, the majority here) -> sunflower / phyllotaxis
  packing: O(N), deterministic, no overlaps.
- Each tiny connected cluster -> its own Fruchterman-Reingold run: O(comp^2),
  independent of total N.
- Pack clusters in an outer phyllotaxis ring around the isolate field so nothing
  overlaps.

Deterministic (seeded) and linear in N. Pure stdlib.
"""

import argparse
import json
import math
import random
import sys
import time
from collections import defaultdict
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import couchdb_client  # noqa: E402

GOLDEN_ANGLE = math.pi * (3.0 - math.sqrt(5.0))  # ~2.399963 rad


def load_nodes(path):
    with open(path, "r", encoding="utf-8") as fh:
        raw = json.load(fh)
    arr = raw if isinstance(raw, list) else raw.get("nodes", raw.get("categories", []))
    nodes = []
    for i, rec in enumerate(arr):
        if not isinstance(rec, dict):
            continue
        nid = rec.get("id") or rec.get("_id")
        if nid is None or nid == "":
            nid = "node.%d" % i
        nodes.append(str(nid))
    return nodes, arr


def load_nodes_from_couch():
    """Pull all node docs from CouchDB. Returns (node_ids, docs) like load_nodes."""
    docs = couchdb_client.all_docs()
    nodes = []
    arr = []
    for i, rec in enumerate(docs):
        if not isinstance(rec, dict):
            continue
        nid = rec.get("id") or rec.get("_id")
        if nid is None or nid == "":
            nid = "node.%d" % i
        nodes.append(str(nid))
        arr.append(rec)
    return nodes, arr


def build_edges(arr, node_set):
    """Undirected edges between existing node ids, from relationship_set."""
    edges = set()
    for rec in arr:
        if not isinstance(rec, dict):
            continue
        sid = rec.get("id")
        if sid is None:
            continue
        sid = str(sid)
        if sid not in node_set:
            continue
        rels = rec.get("relationship_set") or rec.get("relationships") or []
        for rel in rels:
            if not isinstance(rel, dict):
                continue
            tid = rel.get("targetNodeId") or rel.get("target")
            if tid is None:
                continue
            tid = str(tid)
            if tid == sid or tid not in node_set:
                continue
            edges.add(tuple(sorted((sid, tid))))
    return edges


class UnionFind:
    def __init__(self, items):
        self.parent = {x: x for x in items}

    def find(self, x):
        root = x
        while self.parent[root] != root:
            root = self.parent[root]
        while self.parent[x] != root:
            self.parent[x], x = root, self.parent[x]
        return root

    def union(self, a, b):
        ra, rb = self.find(a), self.find(b)
        if ra != rb:
            self.parent[ra] = rb

    def components(self):
        groups = defaultdict(list)
        for x in self.parent:
            groups[self.find(x)].append(x)
        return list(groups.values())


def fruchterman_reingold(members, edge_pairs, spacing, iterations, rng):
    """Classic FR for one small component. Returns {id: (x, y)} centered at origin."""
    n = len(members)
    idx = {nid: i for i, nid in enumerate(members)}
    # Seed on a circle with tiny deterministic jitter (avoids degenerate d=0).
    r0 = spacing * 0.5
    xs = [r0 * math.cos(2 * math.pi * i / n) + rng.uniform(-1.0, 1.0) for i in range(n)]
    ys = [r0 * math.sin(2 * math.pi * i / n) + rng.uniform(-1.0, 1.0) for i in range(n)]

    k = float(spacing)  # ideal distance
    k2 = k * k
    # Temperature: start ~ a fraction of the component extent, cool linearly.
    temp = spacing * math.sqrt(max(n, 1)) * 0.4
    temp_min = 0.01

    pairs = [(idx[a], idx[b]) for a, b in edge_pairs if a in idx and b in idx]

    for it in range(iterations):
        disp_x = [0.0] * n
        disp_y = [0.0] * n

        # Repulsive (all pairs)
        for i in range(n):
            for j in range(i + 1, n):
                dx = xs[i] - xs[j]
                dy = ys[i] - ys[j]
                d2 = dx * dx + dy * dy
                if d2 < 1e-4:
                    dx = rng.uniform(-0.5, 0.5)
                    dy = rng.uniform(-0.5, 0.5)
                    d2 = dx * dx + dy * dy
                d = math.sqrt(d2)
                force = k2 / d
                fx = (dx / d) * force
                fy = (dy / d) * force
                disp_x[i] += fx
                disp_y[i] += fy
                disp_x[j] -= fx
                disp_y[j] -= fy

        # Attractive (edges)
        for a, b in pairs:
            dx = xs[a] - xs[b]
            dy = ys[a] - ys[b]
            d2 = dx * dx + dy * dy
            if d2 < 1e-4:
                continue
            d = math.sqrt(d2)
            force = d * d / k
            fx = (dx / d) * force
            fy = (dy / d) * force
            disp_x[a] -= fx
            disp_y[a] -= fy
            disp_x[b] += fx
            disp_y[b] += fy

        # Centering gravity (keep cluster compact)
        for i in range(n):
            disp_x[i] -= xs[i] * 0.01
            disp_y[i] -= ys[i] * 0.01

        # Integrate with cooling
        for i in range(n):
            dx = disp_x[i]
            dy = disp_y[i]
            d = math.sqrt(dx * dx + dy * dy)
            if d > 0:
                limit = min(d, temp)
                xs[i] += (dx / d) * limit
                ys[i] += (dy / d) * limit

        temp = max(temp_min, temp * (1.0 - (it + 1) / iterations))

    # Center on centroid.
    cx = sum(xs) / n
    cy = sum(ys) / n
    return {members[i]: (xs[i] - cx, ys[i] - cy) for i in range(n)}


def component_bounds(positions):
    xs = [p[0] for p in positions.values()]
    ys = [p[1] for p in positions.values()]
    cx = sum(xs) / len(xs)
    cy = sum(ys) / len(ys)
    radius = 0.0
    for nid, (x, y) in positions.items():
        radius = max(radius, math.hypot(x - cx, y - cy))
    return cx, cy, radius


def phyllotaxis(index_one_based, c):
    """Sunflower position for the i-th point (i >= 1)."""
    r = c * math.sqrt(index_one_based)
    theta = index_one_based * GOLDEN_ANGLE
    return r * math.cos(theta), r * math.sin(theta)


def compute_layout(nodes, edges, spacing, iterations, seed):
    rng = random.Random(seed)
    node_set = set(nodes)
    uf = UnionFind(nodes)
    for a, b in edges:
        uf.union(a, b)
    comps = uf.components()

    isolates = []
    clusters = []  # (members_set, [edge pairs within component])
    comp_of = {}
    for c in comps:
        if len(c) == 1:
            isolates.append(c[0])
            comp_of[c[0]] = None
        else:
            s = set(c)
            intra = [(a, b) for (a, b) in edges if a in s and b in s]
            clusters.append((sorted(c), s, intra))
            for nid in c:
                comp_of[nid] = len(clusters) - 1

    positions = {}

    # --- Isolates: phyllotaxis field ---
    c_iso = spacing / math.sqrt(math.pi)
    for i, nid in enumerate(sorted(isolates), start=1):
        x, y = phyllotaxis(i, c_iso)
        positions[nid] = (x, y)
    r_iso = c_iso * math.sqrt(max(len(isolates), 1)) if isolates else 0.0

    # --- Clusters: FR internally, then pack in an outer ring ---
    cluster_layouts = []
    max_radius = 0.0
    for members, _s, intra in clusters:
        local = fruchterman_reingold(members, intra, spacing, iterations, rng)
        _cx, _cy, radius = component_bounds(local)
        cluster_layouts.append((members, local, radius))
        max_radius = max(max_radius, radius)

    slot_r = max_radius + spacing  # each cluster fits inside this radius
    pad = spacing
    c_comp = 2.2 * slot_r / math.sqrt(math.pi)  # phyllotaxis spacing ~ 2.2 * slot_r

    for i, (members, local, _radius) in enumerate(cluster_layouts, start=1):
        px, py = phyllotaxis(i, c_comp)
        rad = math.hypot(px, py)
        push = r_iso + slot_r + pad
        if rad > 0:
            px = px * (rad + push) / rad
            py = py * (rad + push) / rad
        else:
            px = push
            py = 0.0
        for nid, (x, y) in local.items():
            positions[nid] = (x + px, y + py)

    # Recenter the whole field on its centroid.
    if positions:
        gx = sum(p[0] for p in positions.values()) / len(positions)
        gy = sum(p[1] for p in positions.values()) / len(positions)
        positions = {nid: (round(x - gx, 2), round(y - gy, 2)) for nid, (x, y) in positions.items()}

    return positions, len(isolates), len(clusters)


def main(argv=None):
    p = argparse.ArgumentParser(
        prog="layout.py",
        description="Precompute a static graph layout (sunflower + per-component FR).",
    )
    here = Path(__file__).resolve().parent
    repo = here.parent
    p.add_argument("--data-file", default=str(repo / "app" / "data" / "data.json"))
    p.add_argument("--source", choices=("couch", "file"), default="couch",
                   help="where to read nodes from (default: couch)")
    p.add_argument("--layout-file", default=str(repo / "app" / "data" / "layout.json"))
    p.add_argument("--seed", type=int, default=42)
    p.add_argument("--spacing", type=float, default=80.0, help="ideal node distance")
    p.add_argument("--iterations", type=int, default=300, help="FR iterations per cluster")
    p.add_argument("--indent", type=int, default=None, help="JSON indent (default: compact)")
    args = p.parse_args(argv)

    data_path = Path(args.data_file)

    t0 = time.time()
    if args.source == "file":
        if not data_path.exists():
            print("ERROR: data file not found: %s" % data_path, file=sys.stderr)
            return 1
        nodes, arr = load_nodes(data_path)
    else:
        try:
            nodes, arr = load_nodes_from_couch()
        except Exception as exc:
            print("ERROR: could not read nodes from CouchDB: %s" % exc, file=sys.stderr)
            return 1

    if not nodes:
        print("ERROR: no nodes found (source=%s)" % args.source, file=sys.stderr)
        return 1
    node_set = set(nodes)
    edges = build_edges(arr, node_set)
    positions, n_iso, n_clusters = compute_layout(
        nodes, edges, args.spacing, args.iterations, args.seed
    )
    dt = (time.time() - t0) * 1000.0

    out_path = Path(args.layout_file)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    payload = {nid: [x, y] for nid, (x, y) in positions.items()}
    with open(out_path, "w", encoding="utf-8") as fh:
        if args.indent:
            json.dump(payload, fh, indent=args.indent, ensure_ascii=False)
        else:
            json.dump(payload, fh, separators=(",", ":"), ensure_ascii=False)

    print(
        "layout: %d nodes (%d isolated, %d clusters, %d edges) -> %s  [%.1f ms]"
        % (len(payload), n_iso, n_clusters, len(edges), out_path, dt)
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
