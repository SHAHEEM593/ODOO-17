# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request


class Event(http.Controller):
    @http.route(['/product_snippets'], type="json", auth="public")
    def events(self):
        product = request.env['product.template'].sudo().search_read([], fields=['name', 'list_price'], limit=10)
        return product
