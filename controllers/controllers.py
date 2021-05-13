# -*- coding: utf-8 -*-
# from odoo import http


# class Royalties(http.Controller):
#     @http.route('/royalties/royalties/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/royalties/royalties/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('royalties.listing', {
#             'root': '/royalties/royalties',
#             'objects': http.request.env['royalties.royalties'].search([]),
#         })

#     @http.route('/royalties/royalties/objects/<model("royalties.royalties"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('royalties.object', {
#             'object': obj
#         })
