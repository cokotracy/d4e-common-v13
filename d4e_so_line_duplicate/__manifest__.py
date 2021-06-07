# -*- coding: utf-8 -*-
{
    'name': "Sale Order Line Duplicate",

    'description': """
        Sale Order Line Duplicate
    """,

    'author': "D4E",
    'website': "https://www.d4e.cool",
    'category': 'Tools',
    'version': '1.0',
    # any module necessary for this one to work correctly sale_management
    'depends': ['base', 'sale_management'],

    # always loaded
    'data': [
        'views/sale_views.xml',
    ],

}
