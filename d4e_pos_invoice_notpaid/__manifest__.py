# -*- coding: utf-8 -*-
{
    'name': "D4E Pos Invoice Not Paid",
    'summary': """Digital4Efficiency - Add a payment method that generate an unpaid posted invoice""",
    'description': """Add a payment method that generate an unpaid posted invoice.""",
    'category': 'Sales/Point Of Sale',
    'version': '13.0.0.1',
    'depends': [
        'point_of_sale',
        ],

    'data': [
        'views/pos_payment_method_views.xml',
        'views/point_of_sale.xml',
    ],
    'post_init_hook': 'create_payment_methode_unpaid_invoice',

}
