from odoo import fields, models


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    float_field = fields.Float(string="Float To Int")
