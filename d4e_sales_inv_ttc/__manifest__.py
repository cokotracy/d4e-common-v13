# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'D4E Sales and Invoices TTC',
    'version': '14.0.0.0.1',
    'category': 'Tools',
    'summary': '',
    'description': "",
    'website': 'https://d4e-ch.odoo.com',
    'depends': ['account','sale_management'],
    'data': [
        # 'security/purchase_security.xml',
        # 'data/digest_data.xml',
        'views/sale_views.xml',
        'views/account_move_views.xml',
    ],

    'installable': True,
    'auto_install': False,
    'application': True,
}
