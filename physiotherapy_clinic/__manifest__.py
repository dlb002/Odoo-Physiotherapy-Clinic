# -*- coding: utf-8 -*-
{
    'name': "Physiotherapy Clinic",
    'summary': """
Clínica de Fisioterapia""",
    'description': """
<h1>Physiotherapy Clinic Management</h1>
    <p>This module helps manage physiotherapy clinic appointments, patients, and treatments.</p>
    <ul>
        <li>Manage patient records</li>
        <li>Book and manage appointments</li>
        <li>Track treatments</li>
    </ul>
""",
    'author': "Daniel López Bermúdez",
    'website': "https://es.linkedin.com/in/daniel-lopez-bermudez",
    # Indicamos que es una aplicación
    'application': True,
    'license': 'MIT',
    'price': 10.00,
    'currency': 'EUR',
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
    ]
}
