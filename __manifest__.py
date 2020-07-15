# -*- coding: utf-8 -*-
{
    'name': "product_uom_conversions",

    'summary': """
        Easily create new units of measure according to common products unit of measures.
        """,

    'description': """
        For some products, like beauty products, its easier for customers to remember units like:
        - Bottle of 450ml
        - Recipient of 250 fl oz
        When decreasing those products from inventory, sometimes you use other unit of measure.
        Example:
        - Enters to the Salon 3 Bootle of 450ml of Keratina
        - During the service, is used 3 fl oz of Keratina
    """,

    'author': "Alian Rigñack",
    'website': "https://alianrignack.blog",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Products',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base',
                'product'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}