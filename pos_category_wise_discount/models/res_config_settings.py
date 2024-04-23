# -*- coding: utf-8 -*-
from odoo import fields, models


class ResConfigSettings(models.TransientModel):
    """ Included new field in pos settings """
    _inherit = 'res.config.settings'

    pos_check = fields.Boolean(related='pos_config_id.pos_check', readonly=False, string="Category Discount Limit")
    pos_category_limit_disc = fields.Float(related='pos_config_id.pos_category_limit_disc', readonly=False)
    pos_discount = fields.Selection([('percentage', 'Percentage'), ('amount', 'Amount')],
                                    related='pos_config_id.pos_discount', readonly=False)
    pos_category_limit_amt = fields.Float(
        related='pos_config_id.pos_category_limit_amt', readonly=False)
    pos_category_limit_cat_ids = fields.Many2many('pos.category',
                                                  related='pos_config_id.pos_category_limit_cat_ids', readonly=False)
