# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name': "Goodmind Group po custom",
    'summary': """
         The module is to group all POs from the same vendor,
         Invoice report changes.
    """,
    'description': """
        Task id:  2667579
        The module is to group all POs from the same vendor,
        Also to mention in the invoice,
        if there are any items that are yet to be delivered.
    """,
    'author': 'Odoo Ps',
    'version': '1.0.0',
    'depends': ['sale_management', 'stock', 'purchase', 'account'],
    'data': [
    ],
    'installable': True,
}
