# -*- coding: utf-8 -*-
from odoo import models, fields, _
import openpyxl
import base64
from io import BytesIO
from odoo.exceptions import UserError


class WizardImport(models.TransientModel):
    """ wizard model"""
    _name = 'import.order.lines'

    file_import = fields.Binary()

    def action_import_wizard(self):
        """ importing to sale order lines from excel"""
        try:
            active_id = self.env.context.get('active_ids')
            sale = self.env['sale.order'].browse(active_id)
            wb = openpyxl.load_workbook(
                filename=BytesIO(base64.b64decode(self.file_import)), read_only=True
            )
            ws = wb.active
            for record in ws.iter_rows(min_row=2, max_row=None, min_col=None, max_col=None, values_only=True):
                if record[0] is not None:
                    products = self.env['product.product'].search([('name', '=', record[0])], limit=1)
                    product_uom = self.env['uom.uom'].search([('name', '=', record[2])], limit=1)
                    if len(products) == 0:
                        print('if')
                        product_created = self.env['product.product'].create({
                            'name': record[0],
                            'description': record[0],
                            'list_price': record[1]
                        })
                        sale.update({
                            'order_line': [fields.Command.create({
                                'product_id': product_created.product_variant_id.id,
                                'name': product_created.name,
                                'price_unit': record[1],
                                'product_uom': product_uom.id,
                                'product_uom_qty': 1 if record[4] == None else record[4],

                            })]
                        })
                    elif record[3] is None:
                        print('elif1')
                        sale.update({
                            'order_line': [fields.Command.create({
                                'product_id': products.id,
                                'name': record[0],
                                'price_unit': record[1],
                                'product_uom': product_uom.id,
                                'product_uom_qty': 1 if record[4] == None else record[4],
                            })]
                        })
                    else:
                        print('else')
                        sale.update({
                            'order_line': [fields.Command.create({
                                'product_id': products.id,
                                'name': record[3],
                                'price_unit': record[1],
                                'product_uom': product_uom.id,
                                'product_uom_qty': 1 if record[4] == None else record[4],
                            })]
                        })
        except:
            raise UserError(
                _('Please insert a valid file'))
