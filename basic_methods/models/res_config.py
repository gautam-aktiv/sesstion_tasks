from odoo import models, fields, api

class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    employee_id = fields.Many2one('hr.employee', string="Employee")

    @api.model
    def get_values(self):
        res = super(ResConfigSettings, self).get_values()
        employee_id = self.env['ir.config_parameter'].sudo().get_param('basic_methods.employee_id')
        res.update(
            employee_id=int(employee_id) if employee_id else False
        )
        return res

    def set_values(self):
        super(ResConfigSettings, self).set_values()
        self.env['ir.config_parameter'].sudo().set_param('basic_methods.employee_id', self.employee_id.id if self.employee_id else False)
