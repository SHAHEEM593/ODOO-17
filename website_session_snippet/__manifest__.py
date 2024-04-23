# -*- coding: utf-8 -*-
{
    'name': "Session Snippets",
    'version': '17.0.1.0.0',
    'depends': ['base','website'],
    'author': "Shaheem",
    'category': 'category',
    'description': """
   Session  Snippets 
    """,
    'summary': 'summery',
    # data files always loaded at installation
    'data': [
        'views/website_snippets.xml'
    ],

    'application': True,
    'installable': True,
'assets': {
        'web.assets_frontend': [
            'website_session_snippet/static/src/js/products.js',
            'website_session_snippet/static/src/xml/products_snippets.xml',

        ],


    },
}
