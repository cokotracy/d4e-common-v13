odoo.define('d4e_invoice_print.sidebar', function (require) {
"use strict";

var core = require("web.core");
var Sidebar = require("web.Sidebar");

Sidebar.include({
    currentRecords: [],
    _addRecords: function (model, resID) {
        var self = this;
        if (!resID) {
            return Promise.resolve();
        }
        return self._rpc({
            context: self.env.context,
            model: model,
            method: 'search_read',
            args: [[['id', 'in', resID]]],
        }).then(function (r) {
            self.currentRecords = r;
        });
    },
    _showItem: function (item) {
        var tab = [];
        if (item.classname) {
            tab = item.classname.split(' ');
        }
        tab.splice(tab.indexOf('d-none'), 1);
        item.classname = tab.join(' ');
    },
    _hideItem: function (item) {
        var tab = [];
        if (item.classname) {
            tab = item.classname.split(' ');
        }
        tab.push('d-none');
        item.classname = tab.join(' ');
    },
    _condition: function (record, item) {
        return this.env.model === 'account.move' && ((record && (record.state === 'draft' || record.type === 'in_invoice')) || this.env.context.default_type === 'in_invoice') && item.label === "Imprimer avec la facture QR";
    },
    _manageItemBefore: function () {
        var self = this;
        for (var i = 0; i < self.items.other.length; i++) {
            var item = self.items.other[i], rec = null;
            if (!_.isEmpty(self.currentRecords) && self.currentRecords.length === 1) {
                var rec = self.currentRecords[0];
            }
            if (self._condition(rec, item)) {
                self._hideItem(item);
            } else {
                self._showItem(item);
            }
        }
    },
    _redraw: function () {
        var self = this, def = self._addRecords(self.env.model, self.env.activeIds).then(function () {
            self._manageItemBefore();
        });
        return Promise.resolve(def).then(self._super.bind(self));
    },
});

});
