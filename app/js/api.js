/*
 * API access for the Tecnica renderer (graph.html / edit.html).
 *
 * All data is served by the sync server (bin/sync.py); the browser never
 * talks to CouchDB directly. Relative same-origin endpoints:
 *
 *   - GET api/nodes  -> flat node array (the server proxies CouchDB,
 *                       strips _id/_rev and skips the layout doc)
 *   - GET api/layout -> positions {nodeId: [x, y]} (CouchDB layout doc,
 *                       static layout.json as server-side fallback)
 *
 * loadLayout() also tries the static data/layout.json directly as a
 * last resort when the server is unreachable.
 */
(function (global) {
    'use strict';

    /**
     * Fetch every node document via the sync server. Returns the same flat
     * array shape the renderer has always consumed.
     */
    async function loadNodes() {
        var res = await fetch('api/nodes', { headers: { 'Accept': 'application/json' } });
        if (!res.ok) throw new Error('API HTTP ' + res.status);
        var body = await res.json();
        if (!Array.isArray(body)) throw new Error('api/nodes: expected a JSON array');
        return body;
    }

    /**
     * Fetch the precomputed layout ({ nodeId: [x, y] }).
     *
     * Primary source is the sync server's GET /api/layout. If the sync
     * server is unreachable, try the static file as a last resort.
     * Resolves to a positions map, or null if nothing loads (the caller
     * then falls back to random placement).
     */
    async function loadLayout() {
        var urls = ['api/layout', 'data/layout.json'];
        for (var i = 0; i < urls.length; i++) {
            try {
                var res = await fetch(urls[i], { headers: { 'Accept': 'application/json' } });
                if (res.ok) {
                    var body = await res.json();
                    if (body && typeof body === 'object' && Object.keys(body).length) return body;
                }
            } catch (e) { /* try next source */ }
        }
        return null;
    }

    global.Api = { loadNodes: loadNodes, loadLayout: loadLayout };
})(window);
