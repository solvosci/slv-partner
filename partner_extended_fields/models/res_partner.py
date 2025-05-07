# © 2025 Solvos Consultoría Informática (<http://www.solvos.es>)
# License LGPL-3.0 (https://www.gnu.org/licenses/lgpl-3.0.html)

from odoo import models, fields


class ResPartner(models.Model):
    _inherit = "res.partner"

    has_container = fields.Boolean()
