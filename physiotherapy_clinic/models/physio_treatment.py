# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError

class PhysioTreatment(models.Model):
    """
    Esta clase representa un tratamiento.
    """
    _name = 'physio.treatment'
    _description = 'Tratamiento'

    name = fields.Char(string="Nombre", required=True)
    description = fields.Char(string="Descripción")
    price = fields.Float(string="Precio", required=True)
    duration = fields.Integer(string="Duracion", required=True)
    date_ids = fields.One2many(comodel_name="physio.date", inverse_name="treatment_id", string="Historial de citas")

    @api.constrains('price')
    def _check_price(self):
        """No permitir precios negativos"""
        for record in self:
            if record.price < 0:
                raise ValidationError("El precio del tratamiento debe ser mayor o igual a 0.")

    @api.constrains('duration')
    def _check_duration(self):
        """No permitir duraciones negativas o cero"""
        for record in self:
            if record.duration <= 0:
                raise ValidationError("La duración del tratamiento debe ser mayor a 0 minutos.")