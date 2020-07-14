# -*- coding: utf-8 -*-
from odoo import http

# class ProductUomConversions(http.Controller):
#     @http.route('/product_uom_conversions/product_uom_conversions/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/product_uom_conversions/product_uom_conversions/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('product_uom_conversions.listing', {
#             'root': '/product_uom_conversions/product_uom_conversions',
#             'objects': http.request.env['product_uom_conversions.product_uom_conversions'].search([]),
#         })

#     @http.route('/product_uom_conversions/product_uom_conversions/objects/<model("product_uom_conversions.product_uom_conversions"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('product_uom_conversions.object', {
#             'object': obj
#         })