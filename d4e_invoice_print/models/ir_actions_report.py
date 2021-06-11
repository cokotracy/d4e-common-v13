# -*- coding: utf-8 -*-
from odoo import models, fields, http


class Report(models.Model):
    _inherit = 'ir.actions.report'

    def report_action(self, docids, data=None, config=True):
        res = super(Report, self).report_action(docids=docids, data=data, config=config)
        if self == self.env.ref('account.account_invoices'):
            active_ids = self.env['account.move'].sudo()
            if docids:
                if isinstance(docids, models.Model):
                    active_ids = docids
                elif isinstance(docids, int):
                    active_ids = active_ids.browse([docids])
                elif isinstance(docids, list):
                    active_ids = active_ids.browse(docids)
            active_ids.update_print_date()
        return res
