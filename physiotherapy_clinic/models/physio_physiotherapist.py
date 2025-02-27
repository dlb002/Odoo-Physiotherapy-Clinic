# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError
import re

class PhysioPhysiotherapist(models.Model):
    _name = 'physio.physiotherapist'
    _description = 'Fisioterapeuta'

    name = fields.Char(string="Nombre", required=True)
    telephone = fields.Char(string="Teléfono", required=True)
    email = fields.Char(string="Email", default="")
    date_ids = fields.One2many(comodel_name="physio.date", inverse_name="physiotherapist_id", string="Historial de citas")
    specialty = fields.Char(string="Especialidad", required=True)

    @api.constrains('email')
    def _check_email_format(self):
        """Validar el formato del correo electrónico"""
        email_regex = r'^[\w\.-]+@[\w\.-]+\.\w+$'
        for record in self:
            if record.email and not re.match(email_regex, record.email):
                raise ValidationError("El correo electrónico ingresado no es válido.")
