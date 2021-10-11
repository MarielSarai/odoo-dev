# -*- coding: utf-8 -*-
from typing_extensions import Required
from odoo import models, fields, api

class Session(models.Model):
    _name = 'academy.session'
    _description = 'Session info'

    course_id = fields.Many2one(comodel_name='academy.course',
                                string='Course',
                                ondelete='cascade',
                                required=True)

    name = fields.Char(string='Title', related ='course_id.name')

    instructor_id = fields.Many2one(comodel_name = 'res.partner', string = 'instructor')

    student_ids = fields.Many2one(comodel_name = 'res.partner', string = 'strudents')
    