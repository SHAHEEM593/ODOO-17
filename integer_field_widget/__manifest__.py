{
    'name': "Integer Field Widget",
    'version': '17.0.1.0.0',
    'depends': ['base', 'sale_management'],
    'author': "Shaheem",
    'category': 'category',
    'description': """
   Convert Float Field To Integer
    """,
    'summary': ' Convert Float Field To Integer',
    # data files always loaded at installation
    'data': [
        'views/sale_order_view.xml'
    ],
    'assets': {
        'web.assets_backend': [
            'integer_field_widget/static/src/xml/widget_float_to_int.xml',
            'integer_field_widget/static/src/js/main.js',

        ],

        'application': True,
        'installable': True,

    },

}
