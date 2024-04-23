# -*- coding: utf-8 -*-
from odoo import api, models


class WebsitePublishedMixin(models.AbstractModel):
    _inherit = 'website.searchable.mixin'

    @api.model
    def _search_fetch(self, search_detail, search, limit, order):
        """ search mixin  on website"""
        res = super(WebsitePublishedMixin, self)._search_fetch(search_detail, search, limit, order)
        products = self.env.user.web_product_ids
        if products:
            count = len(products)
            res = (products, count)
        return res
