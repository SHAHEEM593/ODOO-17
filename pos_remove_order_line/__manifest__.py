# -*- coding: utf-8 -*-
{
    'name': "POS Remove Order Line",
    'version': '17.0.1.0.0',
    'depends': ['base','point_of_sale'],
    'author': "Shaheem",
    'category': 'category',
    'description': """
    Pos Remove Order Line
    """,
    'summary': 'Pos Remove Order Line',
    # data files always loaded at installation
    'data': [
    ],

    'application': True,
    'installable': True,

    'assets': {
       'point_of_sale._assets_pos': [
        'pos_remove_order_line/static/src/js/clear_cart.js',
        'pos_remove_order_line/static/src/js/remove_cart.js',
        'pos_remove_order_line/static/xml/pos_order_line.xml',
        'pos_remove_order_line/static/xml/pos_product_screen.xml',
       ],
    },
}
