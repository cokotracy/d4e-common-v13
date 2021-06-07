# -*- coding: utf-8 -*-

from odoo import api, fields, models, _


class ResConfigSettings(models.TransientModel):

    _inherit = 'res.config.settings'

    rounding_id = fields.Many2one(related="company_id.rounding_id", string='Default Cash Rounding', readonly=False)
