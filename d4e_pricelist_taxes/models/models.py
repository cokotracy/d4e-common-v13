# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Pricelist(models.Model):
    _inherit = 'product.pricelist'

    tax_id = fields.Many2one('account.tax', string="Default Tax")
