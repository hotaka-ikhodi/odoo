# -*- coding: utf-8 -*-

from odoo import models, fields, api

class piko(models.Model):
    _inherit =  'product.template'

    @api.model_create_multi
    def create(self, vals_list):
        # Do some business logic, modify vals...
        print("vamosBien")
        # Then call super to execute the parent method
        return super().create(vals_list)