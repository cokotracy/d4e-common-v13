# -*- coding: utf-8 -*-
# from odoo import http


# class D4eInvoiceBank(http.Controller):
#     @http.route('/d4e_invoice_bank/d4e_invoice_bank/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/d4e_invoice_bank/d4e_invoice_bank/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('d4e_invoice_bank.listing', {
#             'root': '/d4e_invoice_bank/d4e_invoice_bank',
#             'objects': http.request.env['d4e_invoice_bank.d4e_invoice_bank'].search([]),
#         })

#     @http.route('/d4e_invoice_bank/d4e_invoice_bank/objects/<model("d4e_invoice_bank.d4e_invoice_bank"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('d4e_invoice_bank.object', {
#             'object': obj
#         })
