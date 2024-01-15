# © 2021 Solvos Consultoría Informática (<http://www.solvos.es>)
# License LGPL-3.0 (https://www.gnu.org/licenses/lgpl-3.0.html)

from odoo import models, api


class ResPartner(models.Model):
    _inherit = "res.partner"

    @api.model
    def name_search(self, name="", args=None, operator="ilike", limit=100):
        res = super(ResPartner, self).name_search(
            name, args=args, operator=operator, limit=limit)
        if name:
            domain = [
                ("vat", operator, name),
            ]
            partner_ids = self._search(domain)
            if partner_ids:
                partner_ids = models.lazy_name_get(self.browse(partner_ids))            
                # TODO optimize removal
                for partner in partner_ids:
                    for record in res:
                        if partner[0] == record[0]:
                            partner_ids.remove(partner)
                if len(partner_ids) > 0:
                    res = partner_ids + res
        return res
