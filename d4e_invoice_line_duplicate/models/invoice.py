# -*- coding: utf-8 -*-

from odoo import models, fields, api


class InvoiceLine(models.Model):
    _inherit = 'account.move.line'

    state = fields.Selection(related='move_id.state', string='State' )

    def copy_inv_line(self):
        line = self.env['account.move.line'].with_context(check_move_validity=False).create({
            'product_id': self.product_id.id,
            'name' : self.name,
            'move_id': self.move_id.id,
            'account_id': self.account_id.id,
            'tax_ids': self.tax_ids.ids,
            'sequence': self.sequence + 1,
            'analytic_account_id': self.analytic_account_id.id,
            'quantity': self.quantity,
            'product_uom_id': self.product_uom_id.id,
            'price_unit': self.price_unit,
            'discount': self.discount,
            'price_subtotal': self.price_subtotal,
        })
        line.move_id._recompute_dynamic_lines(recompute_all_taxes=True, recompute_tax_base_amount=True)