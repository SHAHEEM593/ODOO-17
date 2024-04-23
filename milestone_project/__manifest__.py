# -*- coding: utf-8 -*-
{
    'name': "Milestone",
    'version': '17.0.1.0.0',
    'depends': ['base', 'sale_management','project'],
    'author': "Shaheem",
    'category': 'category',
    'description': """
   Creating Milestone from Order lines
    """,
    'summary': 'summery',
    # data files always loaded at installation
    'data': [
        'views/sale_order.xml',
    ],

    'application': True,
    'installable': True,

}
