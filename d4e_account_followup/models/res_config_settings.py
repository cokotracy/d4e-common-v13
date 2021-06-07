# -*- coding: utf-8 -*-
from odoo import api, fields, models


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    followup_source_doc_visibility = fields.Boolean(string="Followups reports document source visibility")

    def set_values(self):
        super(ResConfigSettings, self).set_values()
        self.env['ir.config_parameter'].set_param('d4e_account_followup.fsdv', self.followup_source_doc_visibility)

    def get_values(self):
        res = super(ResConfigSettings, self).get_values()
        res['followup_source_doc_visibility'] = self.env['ir.config_parameter'].get_param('d4e_account_followup.fsdv')
        return res
