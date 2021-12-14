# © 2021 Solvos Consultoría Informática (<http://www.solvos.es>)
# License LGPL-3.0 (https://www.gnu.org/licenses/lgpl-3.0.html)

from odoo import fields, models


class ResPartner(models.Model):
    _inherit = "res.partner"

    contact_person_id = fields.Many2one(
        string="Contact Person",
        comodel_name="res.partner",
        help="This partner is the contact person for this company",
        domain="[('is_company','=',False)]",
    )
    contact_person_name = fields.Char(related="contact_person_id.name")
    contact_person_email = fields.Char(related="contact_person_id.email")
