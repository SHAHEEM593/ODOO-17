# -*- coding: utf-8 -*-
{
    'name': "Upcoming Events Portal View",
    'version': '17.0.1.0.0',
    'depends': ['base', 'website'],
    'author': "Shaheem",
    'category': 'category',
    'description': """
   Session  Snippets 
    """,
    'summary': 'Upcoming Events Portal View',
    # data files always loaded at installation
    'data': [
        'security/ir.model.access.csv',
        'data/ir_sequence_data.xml',
        'views/events_menu.xml',
        'views/events_view.xml',
        'views/university_view.xml',
        'views/website_events.xml',
        'views/website_events_tree.xml',

    ],

    'application': True,
    'installable': True,

}
