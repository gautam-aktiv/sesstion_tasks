# -*- coding: utf-8 -*-
from odoo import fields, models


class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    sale_order_id = fields.Many2one('sale.order', 'Sale Order')

    def action_sale_purchase_wizard(self):
        """
            a button action will open wizard with default values that we set
            in context for related purchase order.
        """

        context = {
            'default_partner_id': self.partner_id.id,
            'default_note': self.notes,
            'default_delivery_date': self.date_planned,
            'default_purchase_order_id': self.id,
            'default_product_line_ids': [
                fields.Command.create({
                    'product_id': line.product_id.id,
                    'qty': line.product_uom_qty,
                    'price_unit': line.price_unit,
                }) for line in self.order_line
            ]
        }

        return {
            'type': 'ir.actions.act_window',
            'res_model': 'sale.purchase.wizard',
            'view_mode': 'form',
            'target': 'new',
            'context': context,
        }
