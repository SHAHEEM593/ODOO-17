# -*- coding: utf-8 -*-
from odoo import api, fields, models


class Products(models.Model):
    """product model"""
    _name = "material.product"

    name = fields.Char()
    product_material_id = fields.Many2one(comodel_name='material.request.employee', string='product')
    products_id = fields.Many2one(comodel_name='product.product')
    purchase = fields.Selection([('purchase_order', 'Purchase Order'), ('internal_transfer', 'Internal Transfer')])
    from_location = fields.Many2one('stock.location')
    to_location = fields.Many2one('stock.location')

