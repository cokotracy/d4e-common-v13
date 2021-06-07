# -*- coding: utf-8 -*-
{
    'name': "Invoice Line Duplicate",

    'description': """
        Invoice Line Duplicate
    """,

    'author': "D4E",
    'website': "https://www.d4e.cool",
    'category': 'Tools',
    'version': '1.0',
    # any module necessary for this one to work correctly
    'depends': ['base', 'account'],

    # always loaded
    'data': [
        'views/invoice_views.xml',
    ],

}
