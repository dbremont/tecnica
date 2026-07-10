/*
 * socio-graph.js — shared deck.gl renderer for Tecnica.
 *
 * Exposes window.SocioGraph: pure helpers that turn the host's graph state
 * (nodes/edges + a cam) into deck.gl layers. Both graph.html (viewer) and
 * edit.html (editor) drive it from their own state so they render identically.
 *
 * Requires window.deck (vendor/deck.min.js) loaded first.
 *
 * Design for scale (target 100k+ nodes):
 *   - Positions are static, read once from layout.json (no live force sim).
 *   - Visibility filtering is GPU-side via DataFilterExtension (no array rebuild
 *     on filter change; the full dataset stays on the GPU).
 *   - Picking is GPU-side via deck.pickObject — O(1) per pick.
 *   - Labels are LOD'd by zoom + degree so we never render 100k texts.
 */
(function (global) {
  "use strict";

  function D() {
    var d = global.deck;
    if (!d) throw new Error("SocioGraph: window.deck is missing — load vendor/deck.min.js first");
    return d;
  }

  /* ── camera ────────────────────────────────────────────────────────
   * The host owns cam = {x, y, z} with the transform
   *   screen = world * cam.z + {cam.x, cam.y}   (y-down, like Canvas2D).
   * deck's OrthographicView (flipY:false) maps
   *   screen = (world - target) * scale + {W/2, H/2},  scale = 2^zoom.
   * Solving for target/zoom gives the conversion below so the deck view is
   * pixel-identical to the legacy cam. */
  function camToViewState(cam, width, height) {
    var z = Math.max(cam.z, 1e-3);
    return {
      target: [(width / 2 - cam.x) / z, (height / 2 - cam.y) / z, 0],
      zoom: Math.log2(z),
      minZoom: Math.log2(0.05),
      maxZoom: Math.log2(16),
    };
  }

  function worldToScreen(cam, wx, wy) {
    return { x: wx * cam.z + cam.x, y: wy * cam.z + cam.y };
  }
  function screenToWorld(cam, sx, sy) {
    return { x: (sx - cam.x) / cam.z, y: (sy - cam.y) / cam.z };
  }

  /* ── colors ──────────────────────────────────────────────────────── */
  var PALETTE = [
    [197, 185, 152], [93, 173, 168], [196, 120, 99], [129, 162, 196],
    [188, 150, 186], [120, 178, 122], [210, 168, 110], [150, 150, 170],
    [99, 176, 210], [214, 138, 138], [170, 152, 110], [110, 180, 170],
  ];
  var _colorCache = {};
  function categoryColor(name) {
    if (name == null) name = "Unknown";
    if (_colorCache[name]) return _colorCache[name];
    var h = 0;
    for (var i = 0; i < name.length; i++) h = (h * 31 + name.charCodeAt(i)) | 0;
    var c = PALETTE[Math.abs(h) % PALETTE.length];
    _colorCache[name] = c;
    return c;
  }

  /* Lift an rgb triplet toward white by amt (0..1). Used for a subtle,
   * identity-preserving hover accent (never recolours to pure white). */
  function brighten(rgb, amt) {
    return [
      Math.min(255, Math.round(rgb[0] + (255 - rgb[0]) * amt)),
      Math.min(255, Math.round(rgb[1] + (255 - rgb[1]) * amt)),
      Math.min(255, Math.round(rgb[2] + (255 - rgb[2]) * amt)),
    ];
  }

  /* ── node radius (world units), degree-driven like the legacy renderer ── */
  function nodeRadius(n, maxDegree) {
    var t = maxDegree > 0 ? (n.degree || 0) / maxDegree : 0;
    var r = 3 + t * 15;
    if (r < 3) r = 3;
    if (r > 18) r = 18;
    return r;
  }

  /* ── positions: read from precomputed layout, random-in-bounds fallback ── */
  function seedPositions(nodes, layout, bounds) {
    if (!layout) layout = {};
    var minX = Infinity, maxX = -Infinity, minY = Infinity, maxY = -Infinity;
    var placed = 0;
    nodes.forEach(function (n) {
      var p = layout[n.id];
      if (p && isFinite(p[0]) && isFinite(p[1])) {
        n.position = [p[0], p[1]];
        n.x = p[0]; n.y = p[1];
        placed++;
      }
      if (n.position) {
        if (n.position[0] < minX) minX = n.position[0];
        if (n.position[0] > maxX) maxX = n.position[0];
        if (n.position[1] < minY) minY = n.position[1];
        if (n.position[1] > maxY) maxY = n.position[1];
      }
    });
    if (!isFinite(minX)) { minX = -300; maxX = 300; minY = -300; maxY = 300; }
    var bw = Math.max(1, maxX - minX), bh = Math.max(1, maxY - minY);
    var pad = Math.max(bw, bh) * 0.1 + 50;
    var b = {
      minX: minX - pad, maxX: maxX + pad, minY: minY - pad, maxY: maxY + pad,
      width: bw + pad * 2, height: bh + pad * 2,
    };
    // Fallback for ids missing from the layout (e.g. a node added since recompute).
    nodes.forEach(function (n) {
      if (!n.position || !isFinite(n.position[0])) {
        var x = b.minX + Math.random() * b.width;
        var y = b.minY + Math.random() * b.height;
        n.position = [x, y]; n.x = x; n.y = y;
      }
    });
    b.placed = placed;
    return b;
  }

  function computeBounds(nodes) {
    var minX = Infinity, maxX = -Infinity, minY = Infinity, maxY = -Infinity, n = 0;
    nodes.forEach(function (nd) {
      if (!nd.position) return;
      n++;
      if (nd.position[0] < minX) minX = nd.position[0];
      if (nd.position[0] > maxX) maxX = nd.position[0];
      if (nd.position[1] < minY) minY = nd.position[1];
      if (nd.position[1] > maxY) maxY = nd.position[1];
    });
    if (!isFinite(minX)) return { minX: -300, maxX: 300, minY: -300, maxY: 300, width: 600, height: 600 };
    return { minX: minX, maxX: maxX, minY: minY, maxY: maxY,
             width: Math.max(1, maxX - minX), height: Math.max(1, maxY - minY) };
  }

  function fitCam(cam, nodes, width, height, visibleOnly) {
    var v = [];
    nodes.forEach(function (n) { if (!visibleOnly || n.visible) if (n.position) v.push(n); });
    if (!v.length) v = nodes;
    var b = computeBounds(v);
    var pad = 120;
    var gw = Math.max(1, b.width) + pad * 2;
    var gh = Math.max(1, b.height) + pad * 2;
    var z = Math.min(width / gw, height / gh, 1.2);
    cam.z = z;
    cam.x = width / 2 - ((b.minX + b.maxX) / 2) * z;
    cam.y = height / 2 - ((b.minY + b.maxY) / 2) * z;
    return cam;
  }

  /* ── label LOD: proximity-based — labels appear as you zoom close ────
   * A node's name shows only when it is big enough on screen, so the graph
   * is dot-only when zoomed out and names reveal node-by-node as you zoom
   * in. Robust to graph/screen size (no absolute-zoom cutoffs). */
  var LABEL_SCREEN_RADIUS = 11;
  function labelVisibleFor(nd, maxDegree, zoom) {
    return (nodeRadius(nd, maxDegree) * zoom) >= LABEL_SCREEN_RADIUS;
  }

  /* ── layer builder ──────────────────────────────────────────────────
   * opts: { z, hoveredId, selectedId, searchSet, colorFor, radiusMax,
   *        showLabels, edgeOpacityBase } */
  function buildLayers(nodes, edges, nodeMap, opts) {
    var deck = D();
    opts = opts || {};
    var z = opts.z != null ? opts.z : 1;
    var hoveredId = opts.hoveredId, selectedId = opts.selectedId;
    var searchSet = opts.searchSet || {};
    var colorFor = opts.colorFor || function (nd) { return categoryColor(nd.category); };

    var i, nd, maxDegree = opts.radiusMax || 0;
    if (!opts.radiusMax) {
      for (i = 0; i < nodes.length; i++) {
        nd = nodes[i];
        if ((nd.degree || 0) > maxDegree) maxDegree = nd.degree || 0;
      }
      if (maxDegree < 1) maxDegree = 1;
    }

    var filterExt = new deck.DataFilterExtension({ filterSize: 1 });

    /* edges */
    var edgeData = [];
    for (i = 0; i < edges.length; i++) {
      var e = edges[i];
      var s = nodeMap[e.source], t = nodeMap[e.target];
      if (!s || !t || !s.position || !t.position) continue;
      var col = colorFor(s);
      var lsId = opts.linkSourceId;
      var inc = (hoveredId && (e.source === hoveredId || e.target === hoveredId)) ||
                (selectedId && (e.source === selectedId || e.target === selectedId)) ||
                (lsId && (e.source === lsId || e.target === lsId));
      var alpha = inc ? 230 : Math.round(60 + 60 * z);
      if (alpha > 230) alpha = 230;
      edgeData.push({
        source: s.position, target: t.position,
        color: [col[0], col[1], col[2], alpha],
        width: inc ? 2.2 : 1.1,
        visible: e.visible !== false ? 1 : 0,
      });
    }
    var edgesLayer = new deck.LineLayer({
      id: "edges",
      data: edgeData,
      getSourcePosition: function (d) { return d.source; },
      getTargetPosition: function (d) { return d.target; },
      getColor: function (d) { return d.color; },
      getWidth: function (d) { return d.width; },
      widthUnits: "common",
      widthMinPixels: 0.5,
      parameters: { depthTest: false },
      getFilterValue: function (d) { return d.visible; },
      filterRange: [1, 1],
      extensions: [filterExt],
      pickable: false,
      updateTriggers: { getFilterValue: [edgeData.length], getColor: [hoveredId, selectedId] },
    });

    /* nodes */
    var nodesLayer = new deck.ScatterplotLayer({
      id: "nodes",
      data: nodes,
      getPosition: function (d) { return d.position; },
      getRadius: function (d) { return nodeRadius(d, maxDegree); },
      radiusUnits: "common",
      radiusMinPixels: 2,
      getFillColor: function (d) {
        var c = colorFor(d);
        if (hoveredId && d.id === hoveredId) {
          var b = brighten(c, 0.15);
          return [b[0], b[1], b[2], 235];
        }
        return [c[0], c[1], c[2], 235];
      },
      stroked: false,
      getFilterValue: function (d) { return d.visible !== false ? 1 : 0; },
      filterRange: [1, 1],
      extensions: [new deck.DataFilterExtension({ filterSize: 1 })],
      pickable: true,
      pickRadius: 8,
      parameters: { depthTest: false },
      updateTriggers: { getFilterValue: [nodes.length], getFillColor: [hoveredId] },
    });

    /* highlight rings (stackable): selected (gold), search (cyan), linkSource (plum), hover (white) */
    var lsId = opts.linkSourceId;
    var rings = [];
    for (i = 0; i < nodes.length; i++) {
      nd = nodes[i];
      if (nd.visible === false) continue;
      var baseR = nodeRadius(nd, maxDegree);
      if (nd.id === selectedId) rings.push({ position: nd.position, color: [196, 185, 152, 255], radius: baseR + 5, width: 2.5 });
      if (searchSet[nd.id]) rings.push({ position: nd.position, color: [77, 212, 196, 230], radius: baseR + 7, width: 2 });
      if (nd.id === lsId) rings.push({ position: nd.position, color: [155, 126, 176, 200], radius: baseR + 6, width: 1.6 });
      if (nd.id === hoveredId) rings.push({ position: nd.position, color: [255, 255, 255, 64], radius: baseR + 2, width: 1.0 });
    }
    var ringsLayer = new deck.ScatterplotLayer({
      id: "rings",
      data: rings,
      getPosition: function (d) { return d.position; },
      getRadius: function (d) { return d.radius; },
      radiusUnits: "common",
      getFillColor: [0, 0, 0, 0],
      stroked: true,
      getLineColor: function (d) { return d.color; },
      getLineWidth: function (d) { return d.width || 1.8; },
      lineWidthUnits: "pixels",
      parameters: { depthTest: false },
      pickable: false,
    });

    /* labels — proximity LOD: a name shows only when its node is close
       enough (big on screen), plus any node the user is interacting with. */
    var labelData = [];
    for (i = 0; i < nodes.length; i++) {
      nd = nodes[i];
      if (nd.visible === false) continue;
      var nm = nd.name;
      if (!nm) continue;                       // render only real node names
      var interacting = (hoveredId && nd.id === hoveredId) ||
                        (selectedId && nd.id === selectedId) ||
                        (!!searchSet[nd.id]) ||
                        (lsId && nd.id === lsId);
      if (!opts.showLabels && !interacting && !labelVisibleFor(nd, maxDegree, z)) continue;
      labelData.push({ position: nd.position, text: nm, color: colorFor(nd) });
    }
    var labelsLayer = new deck.TextLayer({
      id: "labels",
      data: labelData,
      getPosition: function (d) { return d.position; },
      getText: function (d) { return d.text; },
      getColor: function (d) { return [214, 209, 196, 240]; },
      getSize: function () { return 12; },
      sizeUnits: "pixels",
      getPixelOffset: [0, -14],
      getTextAnchor: "middle",
      getAlignmentBaseline: "bottom",
      outlineWidth: 3,
      outlineColor: [11, 14, 20, 235],
      background: false,
      parameters: { depthTest: false },
      pickable: false,
      updateTriggers: { data: [z, hoveredId, selectedId, opts.showLabels] },
    });

    var _layers = [edgesLayer, nodesLayer, ringsLayer, labelsLayer];
    /* Link-mode rubber band (editor): a single plum line from source to cursor/target. */
    if (opts.link && opts.link.source && opts.link.target) {
      _layers.push(new deck.LineLayer({
        id: "link",
        data: [{ source: opts.link.source, target: opts.link.target }],
        getSourcePosition: function (d) { return d.source; },
        getTargetPosition: function (d) { return d.target; },
        getColor: [155, 126, 176, 180],
        getWidth: 2,
        widthUnits: "pixels",
        widthMinPixels: 1.5,
        parameters: { depthTest: false },
        pickable: false,
      }));
    }
    return _layers;
  }

  /* ── deck factory ────────────────────────────────────────────────── */
  function createDeck(opts) {
    var deck = D();
    opts = opts || {};
    var view = new deck.OrthographicView({ id: "ortho", controller: false, flipY: true });
    var inst = new deck.Deck({
      canvas: opts.canvasId || "graph-canvas",
      width: opts.width,
      height: opts.height,
      views: [view],
      controller: false,
      initialViewState: { target: [0, 0, 0], zoom: 0 },
      layers: [],
      useDevicePixels: true,
      _telemetry: false,
    });
    return inst;
  }

  function setView(deckInst, layers, cam, width, height) {
    deckInst.setProps({
      width: width,
      height: height,
      initialViewState: camToViewState(cam, width, height),
      layers: layers,
    });
  }

  /* O(1) GPU pick. layerIds restricts to the node layer. */
  function pickAt(deckInst, x, y) {
    var info = deckInst.pickObject({ x: x, y: y, radius: 10, layerIds: ["nodes"] });
    return info && info.object ? info.object : null;
  }

  global.SocioGraph = {
    camToViewState: camToViewState,
    worldToScreen: worldToScreen,
    screenToWorld: screenToWorld,
    categoryColor: categoryColor,
    nodeRadius: nodeRadius,
    seedPositions: seedPositions,
    computeBounds: computeBounds,
    fitCam: fitCam,
    labelVisibleFor: labelVisibleFor,
    buildLayers: buildLayers,
    createDeck: createDeck,
    setView: setView,
    pickAt: pickAt,
  };
})(typeof window !== "undefined" ? window : this);
