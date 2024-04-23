# -*- coding: utf-8 -*-
from odoo import fields, models


class Events(models.Model):
    """ Events"""
    _name = 'events'

    name = fields.Char(required=True)
    start_date = fields.Date(required=True)
    end_date = fields.Date()
    description = fields.Text()
    university_id = fields.Many2one(comodel_name='university.events')
