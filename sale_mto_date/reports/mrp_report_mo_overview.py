# -*- coding: utf-8 -*-
from odoo import models


class ReportMoOverview(models.AbstractModel):
    _inherit = "report.mrp.report_mo_overview"

    def _get_report_data(self, production_id):
        production = self.env["mrp.production"].browse(production_id)
        res = super()._get_report_data(production_id)
        res["mto_date"] = production.date_finished
        return res
