# -*- coding: utf-8 -*-
from odoo import fields, models


class ProjectTask(models.Model):
    """ project task model"""
    _inherit = 'project.task'

    milestone = fields.Integer()
    sale_order_line_milestone_id = fields.Many2one(comodel_name='sale.order.line')

