# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

# List of contributors:
# Marc Tormo <marc@batista10.cat>
# Ian Martorell <ianmartorell@gmail.com>

{
    "name" : "Andorra - Accounting",
    "version" : "18.0.1.0.0",
    "author" : "Batista10",
    'category': 'Accounting/Localizations',
    "description": """
Andorra Comptes Comptables 
==========================

    * Creació de grups comptables
    * Creació del Pla General Comptable
    * Creació de taxes Andorranes (IGI, IRPF)
""",
    "depends" : [
        "account",
        "base_iban",
        "base_vat",
    ],
    "data" : [
        'data/account_chart_template_data.xml',
        'data/account.account.template-common.csv',
        'data/account.account.template-full.csv',
        'data/account_chart_template_account_account_link.xml',
        'data/account_group_data.xml',
        'data/account_tag_data.xml',
        'data/account_tax_group_data.xml',
        'data/account_tax_template_data.xml',
        'data/account_tax_data.xml',
        'data/account.fiscal.position.template-ad.csv',
        'data/account_chart_template_configure_data.xml',
    ],
    'license': 'AGPL-3',
}
