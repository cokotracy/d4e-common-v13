# -*- coding: utf-8 -*-

from odoo import api, fields, models, _


class SaleSubscription(models.Model):
    _inherit = "sale.subscription"

    def recurring_invoice(self):
        ctx = self.env.context.copy()
        ctx.update({'default_invoice_cash_rounding_id': self.company_id.rounding_id})
        res = super(SaleSubscription, self.with_context(ctx)).recurring_invoice()
        return res
