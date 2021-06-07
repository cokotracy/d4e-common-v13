# -*- coding: utf-8 -*-

{
    'name': "Subscriptions Round",

    'description': """
       Define a Default Cash Rounding Method on the invoice created by Subscription.
    """,

    'author': "D4E",
    'website': "https://www.d4e.cool",
    'category': 'Tools',
    'version': '13.0',

    # any module necessary for this one to work correctly
    'depends': [
        'account', 'sale_subscription'
     ],

    # always loaded
    'data': [
        'views/views.xml',
    ],
}