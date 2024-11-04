from odoo import models, fields, api

class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    employee_id = fields.Many2one('hr.employee', string="Employee")

    @api.model
    def get_values(self):
        res = super(ResConfigSettings, self).get_values()
        return res
