from datetime import date

from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    sent_date = fields.Date('Sent Date')

    def mark_as_sent(self):
        self.write({
            'state': 'sent',
            'sent_date': date.today()
        })

    @api.returns('mail.message', lambda value: value.id)
    def message_post(self, **kwargs):
        if self.env.context.get('mark_so_as_sent'):
            self.filtered(lambda o: o.state == 'draft').with_context(
                tracking_disable=True).write({'sent_date': date.today()})
        return super(SaleOrder, self.with_context(mail_post_autofollow=True)).message_post(**kwargs)