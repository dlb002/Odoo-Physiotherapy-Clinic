# Odoo-Physiotherapy-Clinic

Este módulo de Odoo está diseñado para la gestión de clínicas de fisioterapia. Permite la administración de citas, pacientes, fisioterapeutas y tratamientos.

## Requisitos Previos

Antes de instalar el módulo, asegúrate de cumplir con los siguientes requisitos:

- Odoo 16 instalado en un servidor o en local.
- Acceso a un entorno de desarrollo de Odoo (puede ser un entorno virtual o Docker).
- Dependencias de Python requeridas por Odoo.

## Instalación

Sigue estos pasos para instalar el módulo en tu instancia de Odoo:

1. **Clonar el repositorio en la carpeta de addons de Odoo:**
   ```sh
   cd /opt/odoo/addons
   git clone https://github.com/tu_usuario/Odoo-Physiotherapy-Clinic.git
   ```

2. **Reiniciar el servidor de Odoo:**
   ```sh
   sudo systemctl restart odoo
   ```
   O si ejecutas Odoo manualmente:
   ```sh
   ./odoo-bin -c /etc/odoo/odoo.conf
   ```

3. **Activar el modo desarrollador en Odoo**:
   - Ve a **Configuración > Técnico**.
   - Habilita el modo desarrollador.

4. **Instalar el módulo en Odoo:**
   - Ve a **Apps**.
   - Activa la opción "Actualizar lista de módulos".
   - Busca "Physiotherapy Clinic" y haz clic en "Instalar".

## Uso del Módulo

1. **Gestión de Citas**  
   - Accede al menú "Citas" para programar y gestionar las citas de los pacientes.
   - Define el fisioterapeuta asignado, el tratamiento asignado, el paciente asignado, la fecha programada y el estado de la cita.

2. **Administración de Pacientes**  
   - Agrega, edita y visualiza información de pacientes dentro del módulo.
   - Puedes gestionar el nombre y inf. de contacto, ver las citas asignadas.

3. **Fisioterapeutas**  
   - Administra el personal de fisioterapia con información detallada.
   - Puedes gestionar el nombre, inf. de contacto y su especialidad, y ver las citas asignadas.

4. **Gestión de Tratamientos**  
   - Crea y administra tratamientos para los pacientes.
   - Define el nombre, descripción y precio.
   - Se puede ver las citas asignadas a cada tratamiento.

5. **Reportes en PDF**  
   - Genera informes de citas en formato PDF desde la vista de una cita.

## Licencia

Este módulo se distribuye bajo la licencia [MIT](https://opensource.org/license/MIT).

---

### ¡Gracias por usar Odoo-Physiotherapy-Clinic!
