# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import UserError, ValidationError

class Course(models.Model):
    
    #nombre del modelo
    _name = 'academy.course'
    _description = 'Course Info'

    #campos
    #string = visible para todos los usuarios
    #required no puede estar vacio debe tener un valor predeterminado
    #help formato largo proporciona info que ayuda a los uusarios en la interfaz
    #index bool, crea un indice de base de dtos en la columna
    name = fields.Char(string='Title', required=True)
    description = fields.Text(string='Description')
    level = fields.Selection(string='level',
                            selection=[('beginner', 'Beginner'),
                            ('intermediate', 'Intermediate'),
                            ('advanced', 'Advanced')],
                            copy=False)
    active = fields.Boolean(string='Active', default=True)

    base_price = fields.Float(string='Base Price', default=0.00)

    additional_fee = fields.Float(string='Additional Fee', default=10.00)

    total_price = fields.Float(string='Total price', readonly=True)

    session_ids = fields.One2many(comodel_name="academy.session", 
                                  inverse_name="course_id", 
                                  string="Sessions")

    #calculo
    @api.onchange('base_price','additional_fee')
    def _onchange_total_price(self):
    #en py no se usan corchetes
        if self.base_price < 0.00: 
            raise UserError('Base price cannot be set as Negative')
    
        self.total_price = self.base_price + self.additional_fee
    
    #decoradores
    @api.constrains('additional_fee')
    def check_additional_fee(self):
        for record in self:
            if record.additional_fee < 10.00:
                raise ValidationError('Additional Fees cannot be less than 10.00: %s' % record.additional_fee)

    #campos simples: char, text, boolean, date
    #campos resservados : id unico en su registro
                          #create date fecha de creacion del registo
                          #create uid usuario que creo el registro
                          #write date ultima modificacion del registro 
                          