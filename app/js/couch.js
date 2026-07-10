/*
 * CouchDB data access for the Tecnica renderer (graph.html / edit.html).
 *
 * Reads go straight to CouchDB (CORS enabled via bin/couchdb_setup.py).
 * Writes still go through the sync server (bin/sync.py /api/graph/save),
 * which proxies to CouchDB and resolves _rev server-side.
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
            delete doc._id;
            delete doc._rev;
            out.push(doc);
        });
        return out;
    }

    global.CouchData = { loadNodes: loadNodes, config: CFG };
})(window);
