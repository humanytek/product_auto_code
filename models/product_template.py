from openerp import api, fields, models


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    default_variants_code = fields.Char()
