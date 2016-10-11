# -*- coding: utf-8 -*-

from openerp import models, fields, api

class Course(models.model):
	_name = 'openacademy.course'
	name = fields.Char()
# class openacademy(models.Model):
#     _name = 'openacademy.openacademy'

#     name = fields.Char()