from odoo import models, fields

class Employee(models.Model):
    _inherit = 'hr.employee'

    display_name = fields.Char(string="Display Name", compute="_compute_display_name")

    def _compute_display_name(self):
        for employee in self:
            employee.display_name = f"{employee.name} - {employee.work_email or ''}"
