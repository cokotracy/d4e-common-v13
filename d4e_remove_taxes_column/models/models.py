# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class d4e_remove_taxes_column(models.Model):
#     _name = 'd4e_remove_taxes_column.d4e_remove_taxes_column'
#     _description = 'd4e_remove_taxes_column.d4e_remove_taxes_column'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
