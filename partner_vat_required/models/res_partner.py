# © 2022 Solvos Consultoría Informática (<http://www.solvos.es>)
# License LGPL-3.0 (https://www.gnu.org/licenses/lgpl-3.0.html)

from odoo import _, api, models
from odoo.exceptions import ValidationError


class ResPartner(models.Model):
    _inherit = "res.partner"

    @api.model_create_multi
    def create(self, vals_list):
        if not self.env.context.get("skip_vat_required", False):
            contacts_wo_vat = [
                vals.get("name", _("No name")) for vals in vals_list if not vals.get("vat", False) and not vals.get("parent_id", False)
                ]
            if contacts_wo_vat:
                raise ValidationError(_("VAT is required for the following contacts: %(contact_list)s", contact_list = ", ".join(contacts_wo_vat)))
        return super().create(vals_list)
