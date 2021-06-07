from odoo import models, fields, api, _


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    discount_num = fields.Float('Discount (%)')
    amount_discount = fields.Monetary(
        string='Total Discount',
        store=True,
        readonly=True,
        compute='_amount_all',
        tracking=4
    )
    amount_untaxed_with_disc = fields.Monetary(
        string='Total untaxed',
        store=True,
        readonly=True,
        compute='_amount_all',
        tracking=4
    )

    @api.depends('order_line.price_total', 'order_line.is_discount_line')
    def _amount_all(self):
        super(SaleOrder, self)._amount_all()
        for order in self:
            amount_untaxed = amount_discount = 0.0
            for line in order.order_line:
                amount_untaxed += line.price_subtotal
                amount_discount += line.price_subtotal if line.is_discount_line else 0.0
            order.update({
                'amount_discount': amount_discount,
                'amount_untaxed_with_disc': amount_untaxed - amount_discount
            })

    @api.model
    def create(self, vals):
        res = super(SaleOrder, self.with_context({'create_discount': True})).create(vals)

        if 'discount_num' in vals and vals.get('discount_num') != 0:
            self.env['sale.order.line'].create({
                'product_id': self.env.ref('d4e_discount.product_discount').id,
                'name': _('Discount'),
                'price_unit': - (res.amount_untaxed - res.amount_discount) * res.discount_num / 100,
                'product_uom_qty': 1,
                'is_discount_line': True,
                'order_id': res.id,
                'sequence': 0
               # 'tax_id': [(6, 0, [])]
            })
        return res

    def write(self, vals):
        ctx = self.env.context.copy()
        line_discount = self.order_line.filtered(lambda l: l.is_discount_line is True)
        if self.discount_num == 0 and 'discount_num' in vals and vals.get('discount_num') != 0 and 'create_discount' not in ctx:
            price = - (self.amount_untaxed - self.amount_discount) * vals.get('discount_num') / 100
            line_dicount = (0, 0, {
                'product_id': self.env.ref('d4e_discount.product_discount').id,
                'name': _('Discount'),
                'price_unit': price,
                'product_uom_qty': 1,
                'is_discount_line': True,
                'sequence': 0
            })
            print(price)
            if not vals.get('order_line'):
                vals['order_line'] = []
            vals['order_line'].append(line_dicount)

        elif 'discount_num' in vals and vals.get('discount_num') == 0 and 'create_discount' not in ctx:
            line_discount.unlink()

        if line_discount and 'discount_num' in vals and vals.get('discount_num') != 0:
            print(vals.get('discount_num'))
            self.order_line = [(1, line_discount.id, {
                'price_unit': - (self.amount_untaxed - self.amount_discount) * vals.get('discount_num') / 100,
            })]
        return super(SaleOrder, self).write(vals)


    def _prepare_invoice(self):
        res = super(SaleOrder, self)._prepare_invoice()
        res.update({
            'discount_num': self.discount_num,
        })
        return res


class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    is_discount_line = fields.Boolean('Discount Line')

    def _prepare_invoice_line(self):
        res = super(SaleOrderLine, self)._prepare_invoice_line()
        res.update({
            'is_discount_line': self.is_discount_line,
        })
        return res