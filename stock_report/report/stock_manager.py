# -*- coding: utf-8 -*-
from odoo import models, api


class StockManager(models.AbstractModel):
    """ Abstract model"""
    _name = 'report.stock_report.stock_report_template'

    @api.model
    def _get_report_values(self, docids, data=None):
        return {
            'doc_ids': docids,
            'doc_model': ' stock.report',
            'data': data,
        }
