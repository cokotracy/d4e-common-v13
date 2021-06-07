# -*- coding: utf-8 -*-
from odoo import models, fields, api, _


class Employee(models.Model):
    _inherit = 'hr.employee'

    employee_home_address = fields.Text(string=_("Address"))
    employee_phone = fields.Char(string=_("Phone"))
    employee_private_email = fields.Char(string=_("Email"))
    employee_bank_account = fields.Char(string=_("Bank Account Number"))
    employee_bank_id = fields.Many2one(comodel_name='res.bank',
                                       string=_("Banque"))
