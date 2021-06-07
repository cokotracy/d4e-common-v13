# -*- coding: utf-8 -*-
from odoo import models


class Partner(models.Model):
    _inherit = 'res.partner'

    def get_followup_html(self):
        options = {
            'partner_id': self.id,
            'followup_level': (self.followup_level.id, self.followup_level.delay),
            'keep_summary': True,
            'custom_followup_report': True,
        }
        return self.env['account.followup.report'].with_context(print_mode=True, lang=self.lang or self.env.user.lang).get_html(options)
