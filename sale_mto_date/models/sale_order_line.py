# -*- coding: utf-8 -*-
from odoo import models


class SaleOrderLine(models.Model):
    _inherit = "sale.order.line"

    def _prepare_procurement_values(self, group_id):

        res = super()._prepare_procurement_values(group_id)
        res["mto_expected_date"] = self.order_id.mto_expected_date
        return res
