# -*- coding: utf-8 -*-
{
    'name': 'Basic Methods',
    'version': '17.0.1.0.0',
    'category': 'Other',
    'summary': """
        a custom module describe odoo basic methods with example. 
    """,
    'description': """
        The custom module provides an example of the fundamental
        Odoo techniques.
    """,
    'website': "http://www.aktivsoftware.com",
    'author': "Aktiv Software",
    'depends': [
        'hr_timesheet'
    ],
    'data': [
        'views/res_config_view.xml',
        'views/hr_employee_view.xml'
    ],
    'license': 'LGPL-3',
    'installable': True,
    'auto_install': False,
    'application': False,
}