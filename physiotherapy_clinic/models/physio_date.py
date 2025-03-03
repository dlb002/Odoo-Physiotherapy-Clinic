# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError
from datetime import timedelta

class PhysioDate(models.Model):
    """
    Esta clase representa una cita.
    """
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
    treatment_duration = fields.Integer(string="Duración (minutos)", related="treatment_id.duration", readonly=True)

    @api.constrains('datetime', 'physiotherapist_id', 'treatment_duration', 'patient_id')
    def _check_duplicate_appointment(self):
        """Evitar que un fisioterapeuta o paciente tenga citas superpuestas"""
        for record in self:
            # Calcular la hora final de la cita con duración.
            end_time = record.datetime + timedelta(minutes=record.treatment_duration)

            # Verificación de solapamiento para el fisioterapeuta, solo en el mismo día.
            overlapping_appointments_physio = self.env['physio.date'].search([
                ('physiotherapist_id', '=', record.physiotherapist_id.id),
                ('id', '!=', record.id),  # Excluir la misma cita en caso de edición.
                ('datetime', '>=', record.datetime.date()),  # Solo citas después de la fecha de la nueva cita.
                ('datetime', '<', end_time),  # La nueva cita termina después de la hora de inicio de otras.
            ])

            # Verificación de solapamiento para el paciente, solo en el mismo día.
            overlapping_appointments_patient = self.env['physio.date'].search([
                ('patient_id', '=', record.patient_id.id),
                ('id', '!=', record.id),  # Excluir la misma cita en caso de edición.
                ('datetime', '>=', record.datetime.date()),  # Solo citas después de la fecha de la nueva cita.
                ('datetime', '<', end_time),  # La nueva cita termina después de la hora de inicio de otras.
            ])

            if overlapping_appointments_physio:
                raise ValidationError("El fisioterapeuta ya tiene una cita programada que se solapa con esta.")
            if overlapping_appointments_patient:
                raise ValidationError("El paciente ya tiene una cita programada que se solapa con esta.")


    @api.constrains('datetime', 'state')
    def _check_future_date(self):
        """Validar que la fecha de la cita no sea anterior a la fecha actual. Permite cambiarla si el estado es Realizada o Cancelada"""
        for record in self:
            if record.state not in ['performed', 'cancelled'] and record.datetime and record.datetime < fields.Datetime.now():
                raise ValidationError("No se pueden programar citas en el pasado.")
