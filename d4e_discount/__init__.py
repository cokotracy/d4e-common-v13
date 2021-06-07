from . import models

from odoo import api, SUPERUSER_ID


# def update_discount(cr, registry):
#     env = api.Environment(cr, SUPERUSER_ID, {})
#     sales = env['sale.order'].search([('discount', '=', True)])
#     for s in sales:
#         cr.execute("update sale_order set discount_num=5.0, discount=False where id=%s", (s.id, ))
#     invoices = env['account.move'].search([('discount', '=', True)])
#     for inv in invoices:
#         cr.execute("update account_move set discount_num=5.0, discount=False where id=%s", (inv.id, ))
