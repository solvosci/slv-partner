# © 2023 Solvos Consultoría Informática (<http://www.solvos.es>)
# License LGPL-3.0 (https://www.gnu.org/licenses/lgpl-3.0.html)

from odoo import models, api, _
from odoo.exceptions import ValidationError


class ResPartner(models.Model):
    _inherit = "res.partner"

    def check_permission(self, fields_changed=False):
        if not self.env.user.has_group('partner_security_manager.group_manager_partner'):
            raise ValidationError(
                _("Must have administrator permissions in contacts.")
                + (("\n\n(%s)" % fields_changed) if fields_changed else "")
            )

    @api.model
    def create(self, vals):
        self.check_permission()
        return super().create(vals)

    def write(self, vals):
        """
        Contact updatre could be fired from other model updates (e.g.
        purchase.order).
        So we allow some field changes exceptions, if every field changed
        belogs to exception field list
        """
        fields_allowed = self._fields_change_exceptions()
        fields_changed = list(vals.keys())
        changes_allowed = all(
            field in fields_allowed
            for field in fields_changed
        )
        if not changes_allowed:
            self.check_permission(fields_changed=fields_changed)
        return super().write(vals)

    def unlink(self):
        self.check_permission()
        return super().unlink()

    def _fields_change_exceptions(self):
        """
        Add field names/inherit from this method to increase this exception
        list
        """
        return [
            # added by "purchase", when creating RFQ
            "reminder_date_before_receipt",
            "receipt_reminder_email",
            # added by "auth_signup", when e.g. sending an invoice
            "signup_token", "signup_type", "signup_expiration",
        ]
