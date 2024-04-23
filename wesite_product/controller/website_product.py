# -*- coding: utf-8 -*-
from odoo.http import request
from odoo.tools import lazy
from odoo.addons.website_sale.controllers.main import WebsiteSale, TableCompute


class WebsiteSaleInherit(WebsiteSale):
    def shop(self, page=0, category=None, search='', min_price=0.0, max_price=0.0, ppg=False, **post):
        """ updated products from user"""
        res = super(WebsiteSaleInherit, self).shop(page, category, search, min_price, max_price, ppg, **post)
        products = request.env.user.web_product_ids
        category = request.env.user.web_category_id
        if products or category:
            if category:
                for cat in category:
                    products += request.env['product.template'].search([('public_categ_ids', '=', cat.id)])
            website = request.env['website'].get_current_website()
            website_domain = website.website_domain()
            categs_domain = [('parent_id', '=', False),
                             ('id', 'in', request.env.user.web_category_id.ids)] + website_domain
            if search:
                search_categories = category.search(
                    [('product_tmpl_ids', 'in', products.ids)] + website_domain
                ).parents_and_self
                categs_domain.append(('id', 'in', search_categories.ids))
            categs_domain = [('parent_id', '=', False),
                             ('id', 'in', request.env.user.web_category_id.ids)] + website_domain
            categs = lazy(lambda: category.search(categs_domain))
            if ppg:
                try:
                    ppg = int(ppg)
                    post['ppg'] = ppg
                except ValueError:
                    ppg = False
            if not ppg:
                ppg = website.shop_ppg or 20

            ppr = website.shop_ppr or 4
            pricelist = website.pricelist_id
            fiscal_position_sudo = website.fiscal_position_id.sudo()
            products_prices = lazy(lambda: products._get_sales_prices(pricelist, fiscal_position_sudo))
            cate = res.qcontext.get('category')
            res.qcontext.update({
                'products': products.filtered(lambda x: cate.id in x.public_categ_ids.ids) or products,
                'search_product': products.filtered(lambda x: cate.id in x.public_categ_ids.ids) or products,
                'bins': lazy(lambda: TableCompute().process(
                    products.filtered(lambda x: cate.id in x.public_categ_ids.ids) or products, ppg, ppr)),
                'categories': categs,
                'products_prices': products_prices,
                'get_product_prices': lambda product: lazy(lambda: products_prices[product.id]),

            })
        return res
