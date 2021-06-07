# -*- coding: utf-8 -*-
{
    'name': "Migration Winbiz",

    'description': """
        Migration Winbiz
    """,

    'Author': 'D4E',
    'category': 'Tools',
    'website': 'https://www.d4e.cool',
    'version': '1.0',

    # any module necessary for this one to work correctly
    'depends': ['base','account'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/invoice_views.xml',
    ],
}
