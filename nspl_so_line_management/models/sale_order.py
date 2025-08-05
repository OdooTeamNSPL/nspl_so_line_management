from odoo import models, fields, api


class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    def add_line_after(self):
        """Add a new empty line after current line for product selection"""
        current_sequence = self.sequence

        # Shift all later lines
        lines_after = self.order_id.order_line.filtered(
            lambda l: l.sequence > current_sequence
        ).sorted('sequence')

        for line in lines_after:
            line.sequence += 10

        default_uom = self.env.ref('uom.product_uom_unit', raise_if_not_found=False)
        if not default_uom:
            default_uom = self.env['uom.uom'].search([('category_id.name', '=', 'Unit')], limit=1)

        vals = self.env['sale.order.line'].default_get([
            'name', 'product_uom', 'product_uom_qty', 'price_unit'
        ])

        vals.update({
            'order_id': self.order_id.id,
            'sequence': current_sequence + 5,
            'name': ' ',
            'product_uom_qty': 1.0,
            'price_unit': 0.0,
            'discount': 0.0,
            'order_partner_id': self.order_id.partner_id.id,
            'company_id': self.order_id.company_id.id,
            'currency_id': self.order_id.currency_id.id,
            'state': self.order_id.state,
        })

        if default_uom:
            vals['product_uom'] = default_uom.id

        self.env['sale.order.line'].create(vals)

        return {
            'type': 'ir.actions.client',
            'tag': 'soft_reload',
        }