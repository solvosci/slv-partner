# © 2022 Solvos Consultoría Informática (<http://www.solvos.es>)
# License LGPL-3.0 (https://www.gnu.org/licenses/lgpl-3.0.html)

from odoo import models, api


class ResUsers(models.Model):
    _inherit = "res.users"

    @api.model
    def create(self, vals):
        """
        Prevent required VAT for contact linked with user
        """
        users = self.with_context(skip_vat_required=True)
        return super(ResUsers, users).create(vals)
