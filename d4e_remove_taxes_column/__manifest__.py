# -*- coding: utf-8 -*-
{
    'name': "Remove Taxes Column",

    'description': """
        Remove Taxes Column
    """,

    'Author': 'D4E',
    'category': 'Tools',
    'website': 'https://www.d4e.cool',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','account','web','sale',],

    # always loaded
    'data': [
        'views/views.xml',
        'views/templates.xml',
    ],

}
