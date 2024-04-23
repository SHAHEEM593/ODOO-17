# -*- coding: utf-8 -*-
from odoo import fields, models


class Partner(models.Model):
    """partner model """
    _inherit = 'res.partner'

    web_product_ids = fields.Many2many('product.template', string="product")
    web_category_id = fields.Many2many('product.public.category', string="Category")

