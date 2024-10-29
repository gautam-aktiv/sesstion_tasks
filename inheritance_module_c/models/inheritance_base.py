# -*- coding: utf-8 -*-
from odoo import models


class Partner(models.Model):
    _inherit = "res.partner"

    def base_method(self):
        print("Module C: Method Call before Super")
        super().base_method()
        print("Module C: Method Call after Super")
        return "Module-C Method Return"
