# -*- coding: utf-8 -*-
from odoo import api, fields, models, _


class UniversityEvents(models.Model):
    """ University"""
    _name = 'university.events'

    name = fields.Char(string="University Name", required=True)
    code = fields.Char(string="sequence", copy=False, readonly=True, default=lambda self: _('New'))
    university_type = fields.Selection([('private', 'Private'), ('public', 'Public')])
    university_event_name = fields.Char(string="University Event Name")
    university_event_type = fields.Selection([('private_event', 'Private Event'), ('public_event', 'Public Event')])

    status = fields.Selection([('draft', 'Draft'), ('ongoing', 'Ongoing'), ('expired', 'Expired')],
                              default="draft", )
    events_ids = fields.One2many('events', inverse_name="university_id")
    event_ids = fields.Many2many('events')

    @api.model
    def create(self, vals):
        """sequence creation"""
        vals['code'] = self.env['ir.sequence'].next_by_code(
            'university.events') or _('New')
        res = super(UniversityEvents, self).create(vals)

        return res

    def action_confirm(self):
        """ button to confirm events"""
        self.status = 'ongoing'

    def action_expire_button(self):
        """ button to expire"""
        self.status = 'expired'
