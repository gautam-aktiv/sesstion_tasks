# -*- coding: utf-8 -*-
from odoo import api, fields, models


class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    pricelist_id = fields.Many2one('product.pricelist', 'Pricelist')

    @api.onchange('product_template_id')
    def _onchange_product_id_set_pricelist(self):
        """
        Automatically selects the pricelist with the lowest price for
        the selected product.
        """
        if not self.product_template_id or not self.order_id:
            return

        pricelists = self.env['product.pricelist'].with_context({
            'customer_id': self.order_id.partner_id.id,
            'order_date': self.order_id.date_order
        }).search([
            ('item_ids.product_tmpl_id', '=', self.product_template_id.id),
        ])

        lowest_price = float('inf')
        lowest_pricelist_id = False
        for pricelist in pricelists:
            price = pricelist._get_product_price(
                self.product_id,
                quantity=self.product_uom_qty,
                partner=self.order_id.partner_id
            )
            if price < lowest_price:
                lowest_price = price
                lowest_pricelist_id = pricelist.id

        if lowest_pricelist_id:
            self.pricelist_id = lowest_pricelist_id
        else:
            self.pricelist_id = self.order_id.pricelist_id.id
