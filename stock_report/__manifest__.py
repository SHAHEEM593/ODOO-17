# -*- coding: utf-8 -*-
{
    'name': "Stock Report ",
    'version': '17.0.1.0.0',
    'depends': ['base','stock'],
    'author': "Shaheem",
    'category': 'category',
    'description': """
   Stock Report To Inventory Manager
    """,
    'summary': 'Stock Report To Inventory Manager',
    # data files always loaded at installation
    'data': [
        'security/ir.model.access.csv',
        'data/ir_cron.xml',
        'data/email_template.xml',
        'report/stock_report_template.xml',
        'report/ir_actions_report.xml'
    ],

    'application': True,
    'installable': True,

}
