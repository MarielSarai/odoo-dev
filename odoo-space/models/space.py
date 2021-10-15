# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Space(models.Model):
    
    _name = 'space.odoo'
    _description = 'Space info'
    
    name = fields.Char(string='Nombre', required=True)
    dimension = fields.Char(string='Dimensiones')
    numpasajeros = fields.Char(string='Pasajeros')
    tipobarco = fields.Char(string='Tipo de Barco')
    active = fields.Boolean(string='Active', default=True)