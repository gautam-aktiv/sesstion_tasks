# -*- coding: utf-8 -*-
from odoo import fields, models


class SaleOrder(models.Model):
    _inherit = "sale.order"

    mto_expected_date = fields.Datetime("MTO Expected Date")
