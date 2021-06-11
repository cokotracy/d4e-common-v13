# -*- coding: utf-8 -*-
from odoo import models, fields, http
from odoo.tools import pdf
from datetime import datetime


class AccountMove(models.Model):
    _inherit = 'account.move'

    print_date = fields.Datetime('Print Date')
    printed = fields.Boolean('Printed')
    sent = fields.Boolean('Sent')

    def update_print_date(self):
        for record_id in self:
            if record_id.state != 'draft':
                record_id.write({
                    'print_date': datetime.now(),
                    'printed': True,
                })

    def print_ch_qr_bill(self):
        res = super(AccountMove, self).print_ch_qr_bill()
        self.update_print_date()
        return res

    def isr_print(self):
        res = super(AccountMove, self).isr_print()
        self.update_print_date()
        return res

    def action_invoice_print(self):
        res = super(AccountMove, self).action_invoice_print()
        self.update_print_date()
        return res

    def copy(self, default=None):
        default = dict(default or {})
        default['print_date'] = None
        default['printed'] = None
        return super(AccountMove, self).copy(default=default)

    def _pdf_invoices_with_isr(self, invoice_ids):
        pdf_docs = []
        actions = [
            http.request.env.ref('account.account_invoices'),
            http.request.env.ref('l10n_ch.l10n_ch_isr_report'),
        ]
        for invoice_id in invoice_ids:
            pdf_data = actions[0].render_qweb_pdf(invoice_id)[0]
            pdf_docs.append(pdf_data)
            active_invoice = http.request.env['account.move'].browse(invoice_id)
            if active_invoice and active_invoice.l10n_ch_isr_valid:
                active_invoice.l10n_ch_isr_sent = True
                isr_data = actions[1].render_qweb_pdf(invoice_id)[0]
                pdf_docs.append(isr_data)
            active_invoice.update_print_date()
        pdf_merge = pdf.merge_pdf(pdf_docs)
        return pdf_merge

    def _pdf_invoices_with_qr(self, invoice_ids):
        pdf_docs = []
        actions = [
            http.request.env.ref('account.account_invoices'),
            http.request.env.ref('l10n_ch.l10n_ch_qr_report'),
        ]
        for invoice_id in invoice_ids:
            pdf_data = actions[0].render_qweb_pdf(invoice_id)[0]
            pdf_docs.append(pdf_data)
            active_invoice = http.request.env['account.move'].browse(invoice_id)
            if active_invoice:
                active_invoice.l10n_ch_isr_sent = True
                qr_data = actions[1].render_qweb_pdf(invoice_id)[0]
                pdf_docs.append(qr_data)
            active_invoice.update_print_date()
        pdf_merge = pdf.merge_pdf(pdf_docs)
        return pdf_merge
