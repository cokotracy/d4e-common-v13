# -*- coding: utf-8 -*-

from odoo import models, fields, api

class SaleOrder(models.Model):
    _inherit = "sale.order"


    @api.onchange('pricelist_id')
    def _compute_tax_id(self):
        """
        Trigger the recompute of the taxes if the pricelist is changed on the SO.
        """
        for order in self:
            order.order_line._compute_tax_id()

    @api.depends('order_line.price_total')
    def _amount_all(self):
        """
        Compute the total amounts of the SO.
        """
        for order in self:
            price_list_tax = order.pricelist_id.tax_id
            amount_untaxed = amount_tax = 0.0
            for line in order.order_line:
                if len(line.tax_id.ids) == 1 and price_list_tax.id == line.tax_id.ids[
                    0] and price_list_tax.price_include:
                    amount_untaxed += line.price_subtotal - line.price_tax
                else:
                    amount_untaxed += line.price_subtotal
                amount_tax += line.price_tax
            order.update({
                'amount_untaxed': amount_untaxed,
                'amount_tax': amount_tax,
                'amount_total': amount_untaxed + amount_tax,
            })


class SaleOrderLine(models.Model):
    _inherit = "sale.order.line"


    def _compute_tax_id(self):
        for line in self:
            fpos = line.order_id.fiscal_position_id or line.order_id.partner_id.property_account_position_id
            # If company_id is set, always filter taxes by the company
            taxes = line.product_id.taxes_id.filtered(lambda r: not line.company_id or r.company_id == line.company_id)
            if line.order_id.pricelist_id:
                price_list_tax = line.order_id.pricelist_id.tax_id
                line.tax_id = fpos.map_tax(price_list_tax, line.product_id, line.order_id.partner_shipping_id) if fpos else price_list_tax
            else:
                line.tax_id = fpos.map_tax(taxes, line.product_id, line.order_id.partner_shipping_id) if fpos else taxes


    @api.depends('product_uom_qty', 'discount', 'price_unit', 'tax_id')
    def _compute_amount(self):
        for line in self:
            price_list_tax = line.order_id.pricelist_id.tax_id
            price = line.price_unit * (1 - (line.discount or 0.0) / 100.0)
            taxes = line.tax_id.compute_all(price, line.order_id.currency_id, line.product_uom_qty,
                                            product=line.product_id, partner=line.order_id.partner_shipping_id)
            line.update({
                'price_tax': sum(t.get('amount', 0.0) for t in taxes.get('taxes', [])),
                'price_total': taxes['total_included'],
                'price_subtotal': taxes['total_excluded'],
            })
            if len(line.tax_id.ids) == 1 and price_list_tax.id == line.tax_id.ids[0] and price_list_tax.price_include:
                line.update({'price_subtotal': taxes['total_included']})
            if self.env.context.get('import_file', False) and not self.env.user.user_has_groups(
                    'account.group_account_manager'):
                line.tax_id.invalidate_cache(['invoice_repartition_line_ids'], [line.tax_id.id])
