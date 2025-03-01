# -*- coding: utf-8 -*-
{
    'name': "Physiotherapy Clinic",
    'summary': """
Clínica de Fisioterapia""",
    'description': """
Physiotherapy Clinic Management
    This module helps manage physiotherapy clinic appointments, patients, and treatments.
    
        Manage patient records
        Book and manage appointments
        Track treatments
    
""",
    'author': "Daniel López Bermúdez",
    'website': "https://es.linkedin.com/in/daniel-lopez-bermudez",
    # Indicamos que es una aplicación
    'application': True,
    # En la siguiente URL se indica qué categorías pueden usarse
    # https://github.com/odoo/odoo/blob/17.0/odoo/addons/base/data/ir_module_category_data.xml
    # Vamos a utilizar la categoría Productivity
    'category': 'Productivity',
    'version': '0.1',
    # Indicamos lista de módulos necesarios para que este funcione correctamente
    # En este ejemplo solo depende del módulo "base"
    'depends': ['base'],
    # Esto siempre se carga
    'data': [
        # Este primero indica la politica de acceso del módulo
        'security/ir.model.access.csv',
        # Cargamos las vistas y las plantillas
        'views/physio_views.xml',
        # Se carga el reporte para imprimir las citas.
        'reports/tarea_template.xml',
    ],
    'icon': 'static/description/icon.png',  # Icono
    'images': ['static/description/thumbnail.png'],  # Imagen de portada
    'license': 'LGPL-3',
}
