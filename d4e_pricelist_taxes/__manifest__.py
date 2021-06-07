# -*- coding: utf-8 -*-
{
    'name': "Tax on Picelist",

    'description': """
        Tax on Picelist
    """,

    'author': "D4E",
    'website': "https://www.d4e.cool",
    'category': 'Tools',
    'version': '1.0',

    # any module necessary for this one to work correctly
    'depends': ['base','product','account','sale','account_invoice_pricelist'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'views/sale_report_templates.xml',
        'views/report_invoice.xml',
    ],

}
