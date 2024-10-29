# -*- coding: utf-8 -*-
from odoo import models


class Partner(models.Model):
    _inherit = "res.partner"

    def base_method(self):
        print("Module A: Method Call before Super")
        super(Partner, self).base_method()
        print("Module A: Method Call after Super")
        return "Module-A Method Return"
