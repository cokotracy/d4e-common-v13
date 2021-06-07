# -*- coding: utf-8 -*-
{
    'name': "D4E Account Follow-ups",
    'summary': """
        Digital4Efficiency - Account Follow-ups
    """,
    'description': """
        Account Follow-ups
    """,
    'author': "d4e",
    'website': "http://www.d4e.cool",
    'version': '13.0.0.2',
    'depends': [
        'account_reports',
        'account_followup',
    ],
    'data': [
        'views/templates.xml',
        'views/res_config_settings_views.xml',
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
}
