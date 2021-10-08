# © 2021 Solvos Consultoría Informática (<http://www.solvos.es>)
# License LGPL-3.0 (https://www.gnu.org/licenses/lgpl-3.0.html)

from odoo import models, fields, api


class ResPartner(models.Model):
    _inherit = "res.partner"

    ship = fields.Boolean(index=True)
    ship_name = fields.Char(
        compute="_compute_ship_fields",
        readonly=False,
        store=True,
    )
    ship_features = fields.Html(
        compute="_compute_ship_fields",
        readonly=False,
        store=True,
    )

    @api.depends("ship")
    def _compute_ship_fields(self):
        for ship in self.filtered(lambda x: not x.ship):
            ship.ship_name = False

    @api.depends("ship_name")
    def _compute_display_name(self):
        return super()._compute_display_name()

    def _get_name(self):
        name = super()._get_name()
        if self.ship:
            name = '%s (%s)' % (name, self.ship_name)
        return name

    @api.model
    def _name_search(self, name, args=None, operator="ilike", limit=100, name_get_uid=None):
        res = super(ResPartner, self)._name_search(
            name, args=args, operator=operator, limit=limit, name_get_uid=name_get_uid
        )
        res_ids = list(res)
        if not name:
            return res
        
        partner_ids = list(
            self.env["res.partner"]._search(
            [("ship_name", operator, name)],
            limit=limit,
            access_rights_uid=name_get_uid,
        ))
        if not partner_ids:
            return res_ids

        res_ids.extend(partner_ids)
        res_ids = list(dict.fromkeys(res_ids))
        return res_ids
