# -*- coding: utf-8 -*-
{
    'name': "Bank Statement Reconciliation Undo",

    'description': """
        Bank Statement Reconciliation Undo
    """,

    'author': "D4E",
    'website': "https://www.d4e.cool",
    'category': 'Tools',
    'version': '1.0',

    # any module necessary for this one to work correctly
    'depends': ['base','account'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],

}
