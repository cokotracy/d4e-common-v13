# -*- coding: utf-8 -*-
{
    'name': 'Sale/Invoice Configurable Discount',
    'version': '1.1',
    'description': """
    Configurable discount applied on total untaxed
""",
    'Author': 'D4E',
    'category': 'Tools',
    'website': 'https://www.d4e.cool',
    'depends': [
        'account',
        'sale',
    ],
    'data': [
        'views/sale_views.xml',
        'views/sale_report_templates.xml',
        'views/invoice_views.xml',
        'views/report_invoice.xml',
        'views/res_config_settings_views.xml',
        'data/product_discount.xml',

    ],
    'installable': True,
    'application': False,
    'auto_install': False,
    # 'post_init_hook': 'update_discount',
}
