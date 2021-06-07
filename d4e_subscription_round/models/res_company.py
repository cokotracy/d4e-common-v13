# -*- coding: utf-8 -*-

from odoo import api, fields, models, tools, _


class Company(models.Model):
    _inherit = "res.company"

    rounding_id = fields.Many2one('account.cash.rounding', 'Default Cash Rounding')
