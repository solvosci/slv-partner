# © 2022 Solvos Consultoría Informática (<http://www.solvos.es>)
# License LGPL-3 - See http://www.gnu.org/licenses/lgpl-3.0.html
{
    "name": "Partner Vat Required",
    "summary": """
        Makes VAT required for Partner contacts that don't belong to a user
    """,
    "author": "Solvos",
    "license": "LGPL-3",
    "version": "13.0.1.0.0",
    "category": "Extra Tools",
    "website": "https://github.com/solvosci/slv-partner",
    "depends": ["base"],
    "data": [
        "views/res_partner_view.xml"
    ],
    'installable': True,
}
