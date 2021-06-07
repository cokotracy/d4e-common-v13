# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Invoice(models.Model):
    _inherit = 'account.move'

    bvr_ref = fields.Char('BVR Reference')

    invoice_payment_ref = fields.Char(string='Payment Reference',
                                      index=True, copy=False,
                                      compute='_compute_bvr_ref',
                                      store=True,
                                      help="The payment reference to set on journal items.")

    @api.depends('bvr_ref','name')
    def _compute_bvr_ref(self):
        for inv in self:
            if inv.bvr_ref:
                ch1 = inv.bvr_ref.split('>')
                ch2 = ch1[1].split('+')
                inv.invoice_payment_ref = ch2[0]
            else:
                inv.invoice_payment_ref = inv.name