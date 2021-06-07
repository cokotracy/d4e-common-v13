from odoo import api, fields, models, SUPERUSER_ID, _


class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    def copy_so_line(self):
        line = self.copy({'order_id': self.order_id.id})
