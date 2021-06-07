from odoo import api, fields, models, tools, SUPERUSER_ID, _


class Project(models.Model):
    _name = "project.project"
    _inherit = ['project.project', 'portal.mixin', 'mail.alias.mixin', 'mail.thread', 'mail.activity.mixin', 'rating.parent.mixin']