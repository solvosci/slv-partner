# © 2023 Solvos Consultoría Informática (<http://www.solvos.es>)
# License LGPL-3.0 (https://www.gnu.org/licenses/lgpl-3.0.html)

from odoo import models, api


class ResPartner(models.Model):
    _inherit = "res.partner"

    @api.model
    def create(self, values):
        res = super(ResPartner, self).create(values)
        res._onchange_phone_validation()
        res._onchange_mobile_validation()
        return res
