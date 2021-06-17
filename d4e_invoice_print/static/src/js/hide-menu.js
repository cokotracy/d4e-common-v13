odoo.define('d4e_invoice_print.sidebar', function (require) {
"use strict";

var core = require("web.core");
var Sidebar = require("web.Sidebar");
var rpc = require('web.rpc');
var ajax = require('web.ajax');
var _t = core._t;

Sidebar.include({
    currentRecords: [],
    readRecord: function (model, activeIds) {
        var self = this;
        return rpc.query({
            model: model,
            method: 'search_read',
            args: [[['id', 'in', activeIds]]],
        }).then(function(rec) {
            self.currentRecords = rec;
            return rec;
        });
    },
    start: function () {
        return Promise.resolve(this.readRecord(this.env.model, this.env.activeIds)).then(this._super.bind(this));
    },
    rejectUnwantedSideMenu: function (sectionCode, items) {
        var self = this;
        if (items && sectionCode === 'other' && self.env && self.env.model === 'account.move' && self.env.context && self.env.context.default_type === 'in_invoice') {
            items = _.reject(items, {label: _t("Print invoice with QR")});
        }
        return items;
    },
    _addItems: function (sectionCode, items) {
        return this._super(sectionCode, this.rejectUnwantedSideMenu(sectionCode, items));
    },
});

});
