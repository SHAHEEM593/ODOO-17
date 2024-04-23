# -*- coding: utf-8 -*-
{
    'name': "POS Category Wise Discount",
    'version': '17.0.1.0.0',
    'depends': ['base','point_of_sale'],
    'author': "Shaheem",
    'category': 'category',
    'description': """
   POS category wise discount
    """,
    'summary': 'summery',
    # data files always loaded at installation
    'data': [
        'views/res_config_settings_view.xml',
    ],
    'assets': {
        'point_of_sale._assets_pos': [
        'pos_category_wise_discount/static/src/js/get_all_prices.js',
        ]
    },

    'application': True,
    'installable': True,

}
