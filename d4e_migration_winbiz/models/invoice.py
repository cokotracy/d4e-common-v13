# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Invoice(models.Model):
    _inherit = 'account.move'

    ref_winbiz = fields.Char('Winbiz Reference')
