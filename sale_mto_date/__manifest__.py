# -*- coding: utf-8 -*-
{
    "name": "Sales Order Manufacturing Scheduler",
    "version": "18.0.1.0.0",
    "category": "Sales/Manufacturing",
    "summary": "This module allows you to set manufactuing date from Sales Order",
    "description": """
        This module enhances the Sales Order functionality by adding a new datetime
        field. When a Manufacturing Order is created from a Sales Order, the value from
        this field is used to set the Scheduled End date in the Manufacturing Order.
        Additionally, this information is reflected in the Manufacturing Order overview
        report.
    """,
    "website": "http://www.aktivsoftware.com",
    "author": "Aktiv Software",
    "depends": ["sale_management", "mrp"],
    "data": ["views/sale_order_views.xml"],
    "assets": {
        "web.assets_backend": [
            "sale_mto_date/static/src/components/mo_overview/mrp_mo_overview.xml",
            "sale_mto_date/static/src/components/mo_overview/mrp_mo_overview.js",
            "sale_mto_date/static/src/components/mo_overview_line/mrp_mo_overview_line.js",
        ],
    },
    "license": "LGPL-3",
    "installable": True,
    "auto_install": False,
    "application": False,
}
