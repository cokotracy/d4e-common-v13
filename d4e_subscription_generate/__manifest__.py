# -*- coding: utf-8 -*-
{
    'name': "Generate subscription invoice ",

    'description': """
       Generate subscription invoice 
    """,

    'author': "D4E",
    'website': "https://www.d4e.cool",
    'category': 'Tools',
    'version': '1.0',
    # any module necessary for this one to work correctly sale_management
    'depends': ['base', 'sale_subscription'],

    # always loaded
    'data': [
        'views/subscription_generate_view.xml',
    ],

}
