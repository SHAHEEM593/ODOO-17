# -*- coding: utf-8 -*-
from odoo import fields, models


class PosConfig(models.Model):
    """ Included new field in pos  """
    _inherit = 'pos.config'

    pos_check = fields.Boolean()
    pos_discount = fields.Selection([('percentage', 'Percentage'), ('amount', 'Amount')])
    pos_category_limit_disc = fields.Float()
    pos_category_limit_amt = fields.Float()
    pos_category_limit_cat_ids = fields.Many2many('pos.category', relation='rel_config_res_config')
