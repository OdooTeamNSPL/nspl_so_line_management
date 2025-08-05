# -*- coding: utf-8 -*-
{
    'name': 'Sale Order Line Management',
    'version': '18.0.1.0.0',
    'category': 'Sales',
    'summary': 'Add plus (+) button to easily insert new lines in Sale Orders and Quotations',
    'description': """
Sale Order Line Management
==========================

This module enhances the Sales Order and Quotation forms by adding a plus (+) button 
after each order line, allowing users to quickly insert a new line right at that spot.

Key Features:
-------------
- Plus (+) button after each sale order line
- Quickly insert lines without scrolling to the bottom
- Enhanced usability for large orders
- Compatible with both Quotations and Confirmed Sale Orders
    """,
    'author': 'Namah Softech Private Limited',
    'maintainer': 'Namah Softech Private Limited',
    'contributors': [
        'Vipul Sah',
    ],
    'website': 'https://www.namahsoftech.com',
    'support': 'support@namahsoftech.com',
    'license': 'LGPL-3',
    'depends': [
        'sale_management',
    ],
    'data': [
        'views/sale_order_views.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'nspl_so_line_management/static/src/js/sale_order_line.js',
            'nspl_so_line_management/static/src/css/sale_order_line.css',
        ],
    },
    'images': [
        'static/description/img/banner.png',
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
    'price': 99.99,
    'currency': 'USD',
}
