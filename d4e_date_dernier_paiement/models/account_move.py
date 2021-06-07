# -*- coding: utf-8 -*-

from odoo import api, fields, models, _
import json

class AccountMove(models.Model):
    _inherit = 'account.move'

    date_last_payment = fields.Date('Date last payment', compute='_compute_last_payment_date')
    def _compute_last_payment_date(self):
        for move in self:
            inv_widget_dict = json.loads(move.invoice_payments_widget)
            if inv_widget_dict:
                if inv_widget_dict.get('content') and inv_widget_dict.get('content')[-1].get('date'):
                    date_lst_paye = inv_widget_dict.get('content')[-1].get('date')
                    move.date_last_payment = date_lst_paye
            else:
                move.date_last_payment = False


