# -*- coding: utf-8 -*-
{
    'name': "Bill Payment Mode",

    'description': """
        Retrieve the payment mode on a vendor Bill.
    """,

    'author': "D4E",
    'website': "https://www.d4e.cool",
    'category': 'Tools',
    'version': '1.0',

    # any module necessary for this one to work correctly
    'depends': ['base', 'account'],

    # always loaded
    'data': [
        'views/account_move.xml',
    ],

}
