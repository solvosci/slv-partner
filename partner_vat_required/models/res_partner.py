# © 2022 Solvos Consultoría Informática (<http://www.solvos.es>)
# License LGPL-3.0 (https://www.gnu.org/licenses/lgpl-3.0.html)

from odoo import _, api, models
from odoo.exceptions import ValidationError


class ResPartner(models.Model):
    _inherit = "res.partner"

    @api.model
    def create(self, vals):
        if (
            not vals.get("vat", False)
            and not vals.get("parent_id", False)
            and not self.env.context.get("skip_vat_required", False)
        ):
            raise ValidationError(_("VAT is required for the contact"))
        return super().create(vals)
