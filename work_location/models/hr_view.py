from odoo import api, fields, models
from odoo import tools, _
from odoo.exceptions import ValidationError

class Employee(models.Model):

    _inherit = "hr.employee"
    
    work_location_for_employee=fields.Char("Work Location")