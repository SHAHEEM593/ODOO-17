# -*- coding: utf-8 -*-
from odoo import fields, models


class SaleOrderLine(models.Model):
    """ sale order line model"""
    _inherit = 'sale.order.line'

    milestone = fields.Integer(string='Milestone')

