# -*- coding: utf-8 -*-
from dateutil.relativedelta import relativedelta
from odoo import api, models


class MrpProduction(models.Model):
    _inherit = "mrp.production"

    @api.depends(
        "company_id",
        "date_start",
        "is_planned",
        "product_id",
        "workorder_ids.duration_expected",
    )
    def _compute_date_finished(self):
        """
        This compute field will check if date_finished is already set or not,
         if not it will compute as per manufacturing work flow.
        """
        for production in self:
            if production.date_finished:
                continue
            if (
                not production.date_start
                or production.is_planned
                or production.state == "done"
            ):
                continue
            days_delay = production.bom_id.produce_delay
            date_finished = production.date_start + relativedelta(days=days_delay)
            if production._should_postpone_date_finished(date_finished):
                workorder_expected_duration = sum(
                    self.workorder_ids.mapped("duration_expected")
                )
                date_finished = date_finished + relativedelta(
                    minutes=workorder_expected_duration or 60
                )
            production.date_finished = date_finished
