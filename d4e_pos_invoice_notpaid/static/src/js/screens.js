odoo.define('d4e_pos_invoice_notpaid.screens', function (require) {
"use strict";

var PosScreen = require('point_of_sale.screens').PaymentScreenWidget;
var models = require('point_of_sale.models');

var core = require('web.core');

var QWeb = core.qweb;
var _t = core._t;


models.load_fields('pos.payment.method','unpaid_invoice');

var InvoiceWithoutLayoutWidget = PosScreen.include({
    init: function(parent,options){
        this._super(parent,options);
//        var self = this;
    },

    validate_order: function(force_validation) {
        if (this.order_is_valid(force_validation)) {
            var self = this
            var order = this.pos.get_order();
            var unpaid_invoice = false;
            order.get_paymentlines().forEach(function (line) {
//                unpaid_invoice = unpaid_invoice || (line.payment_method.name == 'Unpaid invoice');
                unpaid_invoice = unpaid_invoice || line.payment_method.unpaid_invoice;
            });
            if (unpaid_invoice){
                var customer = this.unpaid_invoice_customer_verif(order);
                customer.catch(this._handleFailedPushForInvoice.bind(this, order, false));
                customer.then(function(){self.finalize_validation();})
            }else {
                this.finalize_validation();
            }
        }
    },

    unpaid_invoice_customer_verif: function (order) {
        var has_customer = new Promise(function (resolveCustomer, rejectCustomer) {
            if(!order.get_client()){
                rejectCustomer({code:400, message:'Missing Customer', data:{}});
            }else{
                resolveCustomer(order)
            };
        });
        return has_customer
    },

});
return {
    InvoiceWithoutLayoutWidget: InvoiceWithoutLayoutWidget,
};
});