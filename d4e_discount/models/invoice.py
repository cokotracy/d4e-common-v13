from datetime import date

from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError


class AccountMove(models.Model):
    _inherit = 'account.move'

    discount_num = fields.Float('Discount')
    amount_discount = fields.Monetary(
        string='Total Discount',
        store=True,
        readonly=True,
        compute='_compute_amount_disc',
        tracking=4
    )
    amount_untaxed_with_disc = fields.Monetary(
        string='Total untaxed',
        store=True,
        readonly=True,
        compute='_compute_amount_disc',
        tracking=4
    )


    @api.depends(
        'invoice_line_ids.price_subtotal',
        'invoice_line_ids.is_discount_line',
        'invoice_line_ids',
        )
    def _compute_amount_disc(self):
        for move in self:
            amount_untaxed = amount_discount = 0
            for line in move.invoice_line_ids:
                amount_untaxed += line.price_subtotal
                amount_discount += line.price_subtotal if line.is_discount_line else 0.0
            move.update({
                'amount_discount': amount_discount,
                'amount_untaxed_with_disc': amount_untaxed - amount_discount
            })
            move._recompute_dynamic_lines(recompute_all_taxes=True, recompute_tax_base_amount=True)


    @api.model_create_multi
    def create(self, vals):
        ctx = self.env.context.copy()
        ctx['create_discount'] = True
        res = super(AccountMove, self.with_context(ctx)).create(vals)
        if 'discount_num' in vals and vals.get('discount_num') and not res.line_ids:
            self.env['account.move.line'].create({
                'product_id': self.env.ref('d4e_discount.product_discount').id,
                'name': _('Discount'),
                'price_unit': - res.amount_untaxed * res.discount_num / 100,
                'quantity': 1,
                'is_discount_line': True,
                'move_id': res.id,
                'sequence': 0
            })
        return res

    def write(self, vals):
        ctx = self.env.context.copy()
        if self.discount_num == 0 and 'discount_num' in vals and vals.get(
                'discount_num') != 0 and 'create_discount' not in ctx:
            product_discount = self.env.ref('d4e_discount.product_discount')
            line_dicount = (0, 0, {
                'product_id': product_discount.id,
                'name': _('Discount'),
                'price_unit': - self.amount_untaxed * self.discount_num / 100,
                'quantity': 1,
                'is_discount_line': True,
                'sequence': 0,
                'tax_ids': [(6, 0, [t.id for t in product_discount.taxes_id])],
            })
            if not vals.get('invoice_line_ids'):
                vals['invoice_line_ids'] = []
            vals['invoice_line_ids'].append(line_dicount)
        res = super(AccountMove, self).write(vals)

        return res

    @api.onchange('amount_untaxed', 'line_ids', 'invoice_line_ids')
    def change_qty_discount(self):
        line_discount_id = self.invoice_line_ids.filtered(lambda l: l.is_discount_line is True)
        line_inv_discount_id = self.line_ids.filtered(lambda l: l.is_discount_line is True)
        if self.amount_untaxed and line_discount_id:
            line_inv_discount_id.debit = (self.amount_untaxed - self.amount_discount) * self.discount_num / 100
            self._recompute_dynamic_lines()

    @api.onchange('discount_num', 'line_ids', 'invoice_line_ids')
    def change_unlink_line(self):
        line_discount = self.invoice_line_ids.filtered(lambda l: l.is_discount_line is True)
        product_discount = self.env.ref('d4e_discount.product_discount')

        if self.discount_num != 0 and line_discount:
            self.invoice_line_ids = [(1, line_discount.id, {
                'debit': (self.amount_untaxed - self.amount_discount) * self.discount_num / 100,
            })]

        if self.discount_num == 0 and line_discount:
            self.invoice_line_ids = [(2, line_discount[0].id)]

        if self.discount_num != 0 and not line_discount:
            self.invoice_line_ids = [(0, 0, {
                'product_id': product_discount.id,
                'name': _('Discount'),
                'debit': (self.amount_untaxed - self.amount_discount) * self.discount_num / 100,
                'quantity': 1,
                'is_discount_line': True,
                'account_id': self.journal_id.default_debit_account_id.id,
                'tax_ids': [(6, 0, [t.id for t in product_discount.taxes_id])],
                'sequence': 0
            })]
        self._recompute_dynamic_lines()


class AccountMoveLine(models.Model):
    _inherit = 'account.move.line'

    is_discount_line = fields.Boolean('Discount Line')
