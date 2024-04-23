# -*- coding: utf-8 -*-
{
    'name': "Website Product Visibility",
    'version': '17.0.1.0.0',
    'depends': ['base', 'website'],
    'author': "Shaheem",
    'category': 'category',
    'description': """
   Managing Website Products On Res Partner
    """,
    'summary': 'Website Product Visibility',
    # data files always loaded at installation
    'data': [
        'views/res_partner_view.xml',
    ],

    'application': True,
    'installable': True,

}
