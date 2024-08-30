from odoo import fields, models

class Book(models.Model):
  _name = "library.book"
  _description = "Book"

  name = fields.Char(string="Title", required=True)
  isbn = fields.Char(string="ISBN")
  active = fields.Boolean(string="Active?", default=True)
  date_published = fields.Date()
  image = fields.Binary(string="Cover")
  publisher_id = fields.Many2one(comodel_name="res.partner", string="Publisher")
  author_ids = fields.Many2many(comodel_name="res.partner", string="Authors")