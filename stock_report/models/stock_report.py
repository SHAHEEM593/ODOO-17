# -*- coding: utf-8 -*-
import base64
from datetime import date
from odoo import models


class StockReport(models.Model):
    """ stock report model"""
    _name = 'stock.report'

    def scheduled_stock_report(self):
        """scheduled action to retrieve data and send mail"""
        invoice_report = self.env.ref('stock_report.action_report_product_template')
        query = """select  sq.id,quantity,lo.name as s_no ,pp.name from stock_quant as sq inner join product_template 
        as pp on pp.id = sq.product_id left join product_product as pro on pro.product_tmpl_id = pp.id left join stock_lot 
        as lo on lo.product_id = pro.id"""
        self.env.cr.execute(query)
        report = self.env.cr.dictfetchall()
        today = date.today()
        warehouse = self.env['stock.warehouse'].search([('company_id', '=', self.env.user.company_id.id)])
        warehouse_company = warehouse.name
        data = {'report': report, 'today': today, 'warehouse_company': warehouse_company}
        data_record = base64.b64encode(self.env['ir.actions.report'].sudo()._render_qweb_pdf(
            invoice_report, [False], data=data)[0])
        ir_values = {
            'name': 'Stock ',
            'type': 'binary',
            'datas': data_record,
            'store_fname': data_record,
            'mimetype': 'application/pdf',
            'res_model': 'stock.report',
        }
        invoice_report_attachment_id = self.env[
            'ir.attachment'].sudo().create(
            ir_values)
        if invoice_report_attachment_id:
            email_template = self.env.ref(
                'stock_report.email_template_stock_report')
            mail = self.env.ref('stock.group_stock_manager').users.mapped('email')  # ['','']
            email_values = {
                'email_to': mail[0],
                'email_cc': mail.pop(0),
                'scheduled_date': False,
                'recipient_ids': [],
                'partner_ids': [],
                'auto_delete': True,
            }

        email_template.attachment_ids = [
            (4, invoice_report_attachment_id.id)]
        email_template.with_context(partner='op',
                                    inv=self).send_mail(
            self.id, email_values=email_values, force_send=True)
        email_template.attachment_ids = [(5, 0, 0)]
