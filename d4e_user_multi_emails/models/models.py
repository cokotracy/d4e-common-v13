# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Partner(models.Model):
    _inherit = 'res.partner'

    email_by_company = fields.One2many('user.emails', 'partner_id', 'User Emails by Company')

class Users(models.Model):
    _inherit = 'res.users'


    email_by_company = fields.One2many('user.emails', related="partner_id.email_by_company")

class UserEmails(models.Model):
    _name = 'user.emails'

    partner_id = fields.Many2one('res.partner', 'Partner')
    company_id = fields.Many2one('res.company', 'Company')
    email = fields.Char(string='Email Address')