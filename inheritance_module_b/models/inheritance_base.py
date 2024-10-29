# -*- coding: utf-8 -*-
from odoo import models


class Partner(models.Model):
    _inherit = "res.partner"

    def base_method(self):
        print("Module B: Method Call before Super")
        super().base_method()
        print("Module b: Method Call after Super")
        return "Module-B Method Return"
