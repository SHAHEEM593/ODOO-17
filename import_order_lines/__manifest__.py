# -*- coding: utf-8 -*-
{
    'name': "Import Order Lines",
    'version': '17.0.1.0.0',
    'depends': ['base', 'sale_management'],
    'author': "Shaheem P S ",
    'category': 'category',
    'description': """
    Import Order Lines
    """,
    'summary': 'Manage the sale order lines',
    # data files always loaded at installation
    'data': [
        'security/ir.model.access.csv',
        'views/sale_order.xml',
        'wizard/import_order_lines.xml',
    ],
    'application': True,
    'installable': True,
    "external_dependencies": {"python": ["openpyxl"]}
}
