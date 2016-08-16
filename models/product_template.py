from openerp import _, api, fields, models, exceptions


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    default_variants_code = fields.Char()

    @api.one
    def update_variants_code(self):
        if not self.default_variants_code:
            raise exceptions.ValidationError("The code can not be empty")
        else:
            color = ''
            size = ''
            for product in self.product_variant_ids:
                for attribute in product.attribute_value_ids:
                    if attribute.attribute_id.name == 'Talla':
                        size = attribute.name
                        break
                for attribute in product.attribute_value_ids:
                    if attribute.attribute_id.name == 'Color':
                        color = attribute.name
                        break
                product.default_code = self.default_variants_code + '-' + color + '-' + size
