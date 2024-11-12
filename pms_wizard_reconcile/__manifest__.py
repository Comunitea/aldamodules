# Copyright 2009-2020 Commitsun.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    "name": "PMS Reconcile Payments",
    "author": "Commit [Sun], Odoo Community Association (OCA)",
    "website": "https://github.com/OCA/aldahotels",
    "category": "Generic Modules/Property Management System",
    "version": "14.0.1.0.0",
    "license": "AGPL-3",
    "depends": [
        "pms",
    ],
    "data": [
        "security/ir.model.access.csv",
        "wizard/pms_wizard_reconcile_views.xml",
        "views/account_bank_statement_views.xml",
    ],
    "installable": True,
}
