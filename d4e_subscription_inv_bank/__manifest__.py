# -*- coding: utf-8 -*-
{
    'name': "Bank Account on Subscription Invoice",

    'description': """
        Bank Account on Subscription Invoice
    """,

    'Author': 'D4E',
    'category': 'Tools',
    'website': 'https://www.d4e.cool',
    'version': '1.0',

    # any module necessary for this one to work correctly
    'depends': ['base','sale_subscription'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
}
