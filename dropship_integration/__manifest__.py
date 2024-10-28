# -*- coding: utf-8 -*-
{
    'name': 'Dropshiping Integration',
    'version': '17.0.1.0.0',
    'category': '',
    'summary': """
    """,
    'description': """
    """,
    'website': "http://www.aktivsoftware.com",
    'author': "Aktiv Software",
    'depends': [
        'sale_management',
        'purchase',
        'stock'
    ],
    'data': [
        'security/ir.model.access.csv',
        'wizards/sale_purchase_wizard.xml',
        'views/sale_order_view.xml',
        'views/purchase_order_view.xml',
    ],
    'license': 'LGPL-3',
    'installable': True,
    'auto_install': False,
    'application': False,
}
