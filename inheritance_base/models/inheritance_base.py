# -*- coding: utf-8 -*-
from odoo import models


class Partner(models.Model):
    _inherit = "res.partner"
    _description = "Inheritance Base Class"

    def base_method(self):
        print("\n\n ---------- Call From Base Method ---------- \n\n")
        return "Base Method Return"
