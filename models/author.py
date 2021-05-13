from odoo import api, fields, models

class RoyaltiesAuthor(models.Model):
    _name = "royalties.author"
    _description = "Keep track of the royalties owed/paid to authors."

    author = fields.Char(string='Author', required=True)
    book = fields.Char(string='Book', required=True)

    track = fields.Selection([
        ('yes', 'Yes'),
        ('no', 'No'),
    ], required=True, default='yes')
    
    totalOwed = fields.Float(string="Total Owed", required=False)
    totalPaid = fields.Float(string="Total Paid", required=False)

    note = fields.Text(string='Description')