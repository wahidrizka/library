# -*- coding: utf-8 -*-
# from odoo import http


# class LibaryApp(http.Controller):
#     @http.route('/libary_app/libary_app', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/libary_app/libary_app/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('libary_app.listing', {
#             'root': '/libary_app/libary_app',
#             'objects': http.request.env['libary_app.libary_app'].search([]),
#         })

#     @http.route('/libary_app/libary_app/objects/<model("libary_app.libary_app"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('libary_app.object', {
#             'object': obj
#         })
