# -*- coding: utf-8 -*-

from odoo import api, fields, models, _


class AccountFiscalPosition(models.Model):
    _inherit = 'account.fiscal.position'

    custom_treatment = fields.Boolean("Traitement Personnalisé")