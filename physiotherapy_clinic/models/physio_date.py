# -*- coding: utf-8 -*-
from datetime import datetime

from odoo import models, fields, api
from odoo.exceptions import ValidationError


class PhysioDate(models.Model):
    _name = 'physio.date'
    _description = 'Cita'

    patient_id = fields.Many2one(comodel_name="physio.patient", string="Paciente", required=True)
    physiotherapist_id = fields.Many2one(comodel_name="physio.physiotherapist", string="Fisioterapeuta", required=True)
    datetime = fields.Datetime(string="Fecha y hora", required=True)
    state = fields.Selection(
        [('pending', 'Pendiente'),
         ('confirmed', 'Confirmada'),
         ('performed', 'Realizada'),
         ('cancelled', 'Cancelada')],
        string="Estado",
        default="pending"
    )
    treatment_id = fields.Many2one(comodel_name="physio.treatment", string="Tratamiento", required=True)

    @api.constrains('datetime', 'physiotherapist_id')
    def _check_duplicate_appointment(self):
        """Evitar que un fisioterapeuta tenga dos citas en el mismo horario"""
        for record in self:
            existing_appointment = self.env['physio.date'].search([
                ('physiotherapist_id', '=', record.physiotherapist_id.id),
                ('datetime', '=', record.datetime),
                ('id', '!=', record.id)  # Excluir la misma cita en caso de edición.
            ])
            if existing_appointment:
                raise ValidationError("El fisioterapeuta ya tiene una cita programada en esa fecha y hora.")

    @api.constrains('datetime')
    def _check_future_date(self):
        """Validar que la fecha de la cita no sea anterior a la fecha actual"""
        for record in self:
            if record.datetime and record.datetime < fields.Datetime.now():
                raise ValidationError("No se pueden programar citas en el pasado.")
