# -*- coding: utf-8 -*-
{
    'name': "Material Request",
    'version': '17.0.1.0.0',
    'depends': ['base','sale_management','purchase','stock'],
    'author': "Shaheem P S ",
    'category': 'category',
    'description': """
    the Material Request Module
    """,
    'summary': 'Manage the Material Request',
    # data files always loaded at installation
    'data': [
        'security/res_groups.xml',
        'security/ir_rule.xml',
        'security/ir.model.access.csv',
        'data/ir_sequece_data.xml',
        'views/material_request_menu.xml',
        'views/material_request_employee_view.xml',
        'views/material.product_view.xml'
    ],
    'application': True,
    'installable': True,
}
