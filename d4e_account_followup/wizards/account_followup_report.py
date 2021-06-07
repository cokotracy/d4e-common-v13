# -*- coding: utf-8 -*-
from odoo import models, fields, _


class AccountFollowupReport(models.AbstractModel):
    _inherit = 'account.followup.report'

    def _get_columns_name(self, options):
        headers = super(AccountFollowupReport, self)._get_columns_name(options)
        if options.get('custom_followup_report', False) and headers:
            if not headers[0]:
                headers[0] = {
                    'name': _('Invoice'),
                    'style': 'text-align:center; white-space:nowrap;',
                }
            for header in headers:
                if header['name'] == _('Communication'):
                    header['class'] = 'd-none'
        values = self.env['res.config.settings'].get_values()
        for header in headers:
            if header.get('name', None) == _('Source Document') and not values.get('followup_source_doc_visibility', True):
                header['class'] = 'd-none'
        return headers

    def _get_lines(self, options, line_id=None):
        res = super(AccountFollowupReport, self)._get_lines(options=options, line_id=line_id)
        if options.get('custom_followup_report', False) and self.env.context.get('print_mode', False):
            column_idx = -3
            values = self.env['res.config.settings'].get_values()
            if not values.get('followup_source_doc_visibility', True):
                column_idx -= 1
            for line in res[-10:]:
                columns = line.get('columns', [])
                if columns:
                    for name in [_('Total Due'), _('Total Overdue')]:
                        if columns[-2].get('name', '') == name:
                            columns[column_idx]['name'] = name
        return res

    def get_html(self, options, line_id=None, additional_context=None):
        return super(AccountFollowupReport, self.with_context(partner=options and options.get('partner_id') or False)).get_html(options, line_id=line_id, additional_context=additional_context)

    def _get_report_name(self):
        res = super(AccountFollowupReport, self)._get_report_name()
        if res == _('Followup Report'):
            if self._context.get('partner'):
                if self.env['res.partner'].browse(self._context.get('partner')).followup_level:
                    res = self.env['res.partner'].browse(self._context.get('partner')).followup_level.name
        return res
