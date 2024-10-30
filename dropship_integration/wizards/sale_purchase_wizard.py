# -*- coding: utf-8 -*-
from odoo import api, fields, models


class SalePurchaseWizard(models.TransientModel):
    _name = 'sale.purchase.wizard'
    _description = "Confirm Sale Or Purchase Wizard"

    partner_id = fields.Many2one('res.partner', string='Customer')
    product_line_ids = fields.One2many(
        'product.line.wizard', 'sale_purchase_wizard_id', string='Product'
    )
    note = fields.Html(string='Note')
    delivery_date = fields.Datetime(string='Delivery Date')
    is_dropship = fields.Boolean(
        string='Dropship', store=True,
        compute='_compute_is_dropship'
    )
    sale_order_id = fields.Many2one('sale.order')
    purchase_order_id = fields.Many2one('purchase.order')

    @api.depends('product_line_ids')
    def _compute_is_dropship(self):
        """
        a compute method will compute Boolean value for dropship base on
        product line.
            => if any dropship product available in product line then
            compute as True
        """
        for record in self:
            record.is_dropship = any(
                line.product_id.route_ids.filtered(
                    lambda r: r.name == 'Dropship'
                ) for line in record.product_line_ids
            )

    def action_confirm_from_wizard(self):
        """
            a button method will update details from wizard for specific order
            lines and confirm it.
        """
        so_id = self.sale_order_id
        po_id = self.purchase_order_id

        if so_id:
            so_id.partner_id = self.partner_id
            so_id.note = self.note or ''
            so_id.commitment_date = self.delivery_date or False
            so_id.order_line.unlink()
            for line in self.product_line_ids:
                so_id.order_line.create({
                    'order_id': self.sale_order_id.id,
                    'product_id': line.product_id.id,
                    'product_uom_qty': line.qty,
                    'price_unit': line.price_unit,
                })
            so_id.action_confirm()
            so_id.purchase_order_id = self.env['purchase.order'].search([
                ('sale_order_id', '=', self.sale_order_id.id)
            ], limit=1)

        elif po_id:
            po_id.partner_id = self.partner_id
            po_id.notes = self.note or ''
            po_id.date_planned = self.delivery_date or False
            po_id.order_line.unlink()
            for line in self.product_line_ids:
                po_id.order_line.create({
                    'order_id': self.purchase_order_id.id,
                    'product_id': line.product_id.id,
                    'product_qty': line.qty,
                    'price_unit': line.price_unit
                })
            po_id.button_confirm()


class ProductLineWizard(models.TransientModel):
    _name = 'product.line.wizard'
    _description = "Product Line Wizard"

    sale_purchase_wizard_id = fields.Many2one('sale.purchase.wizard')
    product_id = fields.Many2one('product.product', string='Product')
    qty = fields.Float(string='Quantity')
    price_unit = fields.Float(string='Unit Price')
