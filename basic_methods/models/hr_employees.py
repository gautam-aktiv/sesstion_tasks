# -*- coding: utf-8 -*-
from odoo import api, models, fields

class Employee(models.Model):
    _inherit = 'hr.employee'

    display_name = fields.Char(
        string="Display Name",
        compute="_compute_display_name",
    )
    timesheet_count = fields.Integer(
        string='Timesheet Count',
        compute='_compute_timesheet_count',
    )

    def _compute_display_name(self):
        for employee in self:
            employee.display_name = f"{employee.name}-{employee.work_email or ''}"

    @api.model
    def _name_search(self, name='', args=None, operator='ilike', limit=100, order=None, name_get_uid=None):
        args = args or []
        args += [
            '|', '|', '|', ('name', operator, name),
            ('work_email', operator, name),
            ('work_phone', operator, name),
            ('mobile_phone', operator, name)
        ]
        return self._search(args, limit=limit, access_rights_uid=name_get_uid)

    @api.model
    def _compute_timesheet_count(self):
        for employee in self:
            employee.timesheet_count = \
                self.env['account.analytic.line'].search_count([
                    ('employee_id', '=', employee.id)
                ])

    def action_my_timesheet(self):
        return {
            'name': 'My Timesheets',
            'type': 'ir.actions.act_window',
            'res_model': 'account.analytic.line',
            'view_mode': 'tree,form',
            'target': 'current',
            'domain': [('employee_id', '=', self.id)],
            'context': {
            },
        }
