from odoo import models, fields


class NewModel(models.Model):
    _name = "real.estate"
    _description = " its about real estate"

    name = fields.Char('Name')
    description = fields.Text("Description")
    postcode = fields.Char()
    date_availability = fields.Date(copy=False)
    expected_price = fields.Float()
    selling_price = fields.Float(readonly=True, copy=False)
    bedrooms = fields.Integer(default=True)
    living_area = fields.Float()
    facades = fields.Float()
    garage = fields.Boolean()
    garden = fields.Boolean(default=True)
    garden_area = fields.Boolean()
    active = fields.Boolean(default=True)
    Partner_Id = fields.Many2one('res.partner', string='Customer')
    category_id = fields.Many2many('res.partner',
                                   string='category')  # book_order_ids=fields.One2many('books_order','book_order_id',string='Books')
    state = fields.Selection(string='state',
                             selection=[('new', 'NEW'), ('offerreceived', 'Offer Received'),
                                        ('offeraccepted', 'Offer Accepted'), ('sold', 'Sold'),
                                        ('canceled', 'Canceled')], default='new')


class EstateTag(models.Model):
    _name = "real.estate.tag"
    _description = "tag in estate"

    name = fields.Char('tag', help='Enter  Name')
    active = fields.Boolean(default=True)
    partner_id_tag=fields.Many2one("res.partner",string='partner')
    user_id_tag=fields.Many2many('real.estate',string="user")
    # partner_id_one=fields.One2many('real.estate','Partner_Id',string="one field")
