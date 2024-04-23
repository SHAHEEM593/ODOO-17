# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request


class ServiceRequest(http.Controller):
    @http.route(['/upcoming_events'], type='http', auth="public", website=True, csrf=False)
    def event_request(self):
        """Events"""
        events = request.env['events'].search([]).sudo()
        user = request.env.user.has_group('base.group_user')
        client_url = request.httprequest.host_url
        host = request.env['ir.config_parameter'].sudo().get_param('web.base.url')
        print(host, "*****")
        menu = request.env['ir.ui.menu'].sudo().search([('name', '=', 'Events'), ('parent_id.name', '=', 'Event')])
        menu_id = menu.id
        action = menu.action.id
        values = {
            'client_url': client_url,
            'user': user,
            'host': host,
            'events': events,
            'menu_id': menu_id,
            'action': action
        }
        return request.render("upcoming_event_portal_view.upcoming_events_eve", values)
