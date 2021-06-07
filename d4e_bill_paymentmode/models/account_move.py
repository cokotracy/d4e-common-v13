# -*- coding: utf-8 -*-

from odoo import models, fields, api, _


class AccountMove(models.Model):
    _inherit = "account.move"

    payment_mode = fields.Char(string='Payment Mode', compute='_compute_payment_mode')

    @api.depends('currency_id.name')
    def _compute_payment_mode(self):
        for record in self:
            payment_mode = ''
            if record.type == 'in_invoice' and record.invoice_partner_bank_id:
                if record.invoice_partner_bank_id.acc_type == 'postal':
                    payment_mode = "BVR " + record.currency_id.name
                else:
                    payment_mode = "SEPA " + record.currency_id.name
            record.payment_mode = payment_mode
