/*
 * CouchDB data access for the Tecnica renderer (graph.html / edit.html).
 *
 * Node reads go straight to CouchDB (CORS enabled via bin/couchdb_setup.py).
 * Writes still go through the sync server (bin/sync.py /api/graph/save),
 * which proxies to CouchDB and resolves _rev server-side.
 *
 * Layout reads (loadLayout) hit the sync server's /api/layout first, which
 * serves the CouchDB 'layout' doc with the static layout.json file as
 * fallback; the static file is the last-resort client fallback.
 *
 * Connection is configured via window.COUCHDB = { url, db } — set it before
 * this script loads (e.g. in the page <head>) to point at a non-local install.
 */
(function (global) {
    'use strict';

    var DEFAULTS = { url: 'http://127.0.0.1:5984', db: 'tecnica' };
    var CFG = global.COUCHDB || {};
    CFG.url = (CFG.url || DEFAULTS.url).replace(/\/+$/, '');
    CFG.db = CFG.db || DEFAULTS.db;
    global.COUCHDB = CFG;

    function docsUrl() {
        return CFG.url + '/' + encodeURIComponent(CFG.db) + '/_all_docs?include_docs=true';
    }

    /**
     * True for the computed-layout document (not a graph node).
     */
    function isLayoutDoc(doc) {
        return doc && (doc._id === 'layout' || doc.type === 'layout');
    }

    /**
     * Fetch every node document and return the same flat array shape the
     * renderer always consumed from data.json (CouchDB's _id/_rev stripped).
     * Design docs are skipped.
     */
    async function loadNodes() {
        var res = await fetch(docsUrl(), { headers: { 'Accept': 'application/json' } });
        if (!res.ok) throw new Error('CouchDB HTTP ' + res.status);
        var body = await res.json();
        var out = [];
        (body.rows || []).forEach(function (row) {
            var doc = row.doc;
            if (!doc || typeof doc !== 'object') return;
            if (String(doc._id || '').indexOf('_design') === 0) return;
            if (isLayoutDoc(doc)) return;
            delete doc._id;
            delete doc._rev;
            out.push(doc);
        });
        return out;
    }

    /**
     * Fetch the precomputed layout ({ nodeId: [x, y] }).
     *
     * Primary source is the sync server's GET /api/layout, which reads the
     * CouchDB 'layout' doc and falls back to the static layout file itself.
     * If the sync server is unreachable, try the static file as a last
     * resort. Resolves to a positions map, or null if nothing loads (the
     * caller then falls back to random placement).
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

    global.CouchData = { loadNodes: loadNodes, loadLayout: loadLayout, config: CFG };
})(window);
