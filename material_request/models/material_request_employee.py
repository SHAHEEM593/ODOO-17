# -*- coding: utf-8 -*-
from odoo import api, fields, models, _
from odoo.exceptions import ValidationError


class Employees(models.Model):
    """ request model"""
    _name = "material.request.employee"
    _description = 'employee'
    _rec_name = 'reference'

    reference = fields.Char(string="sequence", copy=False, readonly=True, default=lambda self: _('New'))
    request_id = fields.Many2one('res.partner', string="Request For:", required=True)
    product_ids = fields.One2many('material.product', inverse_name='product_material_id', required=True)
    status = fields.Selection([('draft', 'Draft'), ('waiting_for_approval', 'Waiting for approval'),
                               ('first_approved', 'First Approval '),
                               ('approved_head', 'Approved '), ('reject', 'Reject')])
    active = fields.Boolean(default=True)
    purchase_count = fields.Integer(compute='_compute_purchase_count')
    internal_transfer_count = fields.Integer(compute='_compute_inventory_count')

    @api.model
    def create(self, vals):
        """sequence creation"""
        vals['reference'] = self.env['ir.sequence'].next_by_code(
            'material.request.employee') or _('New')
        res = super(Employees, self).create(vals)
        return res

    def submit_to_manager(self):
        """ action button to submit and create PO And Internal Transfer"""
        for rec in self.product_ids:
            if rec.purchase == 'internal_transfer':
                if rec.from_location:
                    if rec.to_location:
                        self.status = 'waiting_for_approval'
                    else:
                        raise ValidationError('Please  Enter  to location')
                else:
                    raise ValidationError('Please Enter from location')

    def manager_approve(self):
        """action button for manager approval"""
        self.status = 'first_approved'

    def head_approve(self):
        """action button for head approval"""
        self.status = 'approved_head'
        for pro in self.product_ids:
            for product in pro.products_id:
                if pro.purchase == 'purchase_order':
                    for ven in product.seller_ids.partner_id:
                        self.env['purchase.order'].create({
                            'partner_id': ven.id,
                            'origin': self.reference,
                            'order_line': [(fields.Command.create({
                                'product_id': pro.products_id.id,
                            })
                            )]
                        })

                if pro.purchase == 'internal_transfer':
                    warehouse = self.env['stock.warehouse'].search([])
                    internal_transfer = self.env['stock.picking'].create({
                        'partner_id': self.request_id.id,
                        'location_id': pro.from_location.id,
                        'location_dest_id': pro.to_location.id,
                        'picking_type_id': warehouse.in_type_id.id,
                        'origin': self.reference,
                        'move_ids': [(fields.Command.create({
                            'name': '/',
                            'product_id': pro.products_id.id,
                            'location_id': pro.from_location.id,
                            'location_dest_id': pro.to_location.id,
                        })

                        )]

                    })
                    for internal in internal_transfer:
                        print('internal transfer', internal)
                        internal.write({'state': 'done'})

    def head_reject(self):
        """action button for reject"""
        self.status = 'reject'
        self.active = False

    def get_purchase(self):
        """ to get purchase orders """
        for rec in self:
            return {
                'type': 'ir.actions.act_window',
                'name': 'Events',
                'view_mode': 'tree,form',
                'res_model': 'purchase.order',
                'domain': [('origin', '=', rec.reference)],
                'context': "{'create': False}"

            }

    def get_inventory(self):
        """ to get internal transfer """
        for rec in self:
            return {
                'type': 'ir.actions.act_window',
                'name': 'Events',
                'view_mode': 'tree,form',
                'res_model': 'stock.picking',
                'domain': [('origin', '=', rec.reference)],
                'context': "{'create': False}"

            }

    def _compute_purchase_count(self):
        """to get the count of the purchase"""
        for rec in self:
            rec.purchase_count = rec.env['purchase.order'].search_count([('origin', '=', rec.reference)])

    def _compute_inventory_count(self):
        """to get the count of the inventory"""
        for rec in self:
            rec.internal_transfer_count = rec.env['stock.picking'].search_count([('origin', '=', rec.reference)])
