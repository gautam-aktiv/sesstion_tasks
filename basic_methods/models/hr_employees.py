from odoo import api, models, fields

class Employee(models.Model):
    _inherit = 'hr.employee'

    display_name = fields.Char(
        string="Display Name",
        compute="_compute_display_name",
        store=True
    )
    timesheet_count = fields.Integer(
        string='Timesheet Count',
        compute='_compute_timesheet_count',
    )

    @api.depends('name', 'work_email')
    def _compute_display_name(self):
        for employee in self:
            employee.display_name =\
                f"{employee.name} - {employee.work_email or ''}"

    def _compute_timesheet_count(self):
        for employee in self:
            employee.timesheet_count =\
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