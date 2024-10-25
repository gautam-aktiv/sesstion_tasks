# -*- coding: utf-8 -*-
from odoo import api, fields, models


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    pricelist_message = fields.Text()

    @api.onchange('partner_id')
    def _onchange_partner_id(self):
        self._recompute_prices()

    def action_update_prices(self):
        super().action_update_prices()
        self.message_post(body=self.pricelist_message)

    @api.onchange('pricelist_id')
    def _onchange_pricelist_id(self):
        message = (f"you have change price list from"
                   f" {self._origin.pricelist_id.name}"
                   f" to {self.pricelist_id.name}.")
        self.pricelist_message = message
