# -*- coding: utf-8 -*-
{
    'name': "Bank Details on Invoice",

    'description': """
        Bank Details on Invoice
    """,

    'author': "D4E",
    'website': "http://www.d4e.cool",
    'category': 'Tools',
    'version': '1.0',

    # any module necessary for this one to work correctly
    'depends': ['base','account'],

    # always loaded
    'data': [
        'report/report_invoice_bank.xml',
    ],

}
