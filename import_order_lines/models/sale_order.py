# -*- coding: utf-8 -*-
from odoo import models


class SaleOrder(models.Model):
    """ sale order"""
    _inherit = 'sale.order'

    def import_action(self):
        """ import button action for wizard"""
        return {
            'view_mode': 'form',
            'view_type': 'form',
            'res_model': 'import.order.lines',
            'type': 'ir.actions.act_window',
            'target': 'new',
        }
