# -*- coding: utf-8 -*-
# from odoo import http


# class Piko(http.Controller):
#     @http.route('/piko/piko', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/piko/piko/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('piko.listing', {
#             'root': '/piko/piko',
#             'objects': http.request.env['piko.piko'].search([]),
#         })

#     @http.route('/piko/piko/objects/<model("piko.piko"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('piko.object', {
#             'object': obj
#         })
