# -*- coding: utf-8 -*-

from odoo import models, fields, api


class AccountBankStatement(models.Model):
    _inherit = 'account.bank.statement'

    def button_cancel_reconciliations(self):
        for rec in self:
            for line in rec.line_ids:
                print(rec.state)
                print(line.state)
                line.button_cancel_reconciliation()

