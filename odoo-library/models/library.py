# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Library(models.Model):
    
    _name = 'library.odoo'
    _description = 'Library info'
    
    name = fields.Char(string='Nombre del libro', required=True)
    autor = fields.Char(string='Autor', required=True)
    editor = fields.Char(string='Editor', required=True)
    año_edicion = fields.Char(string='Año de edicion', required=True)
    genero = fields.Char(string='Genero', required=True)
    