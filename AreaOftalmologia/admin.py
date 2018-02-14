from django.contrib import admin
from AreaOftalmologia.models import *
from actions import export_as_csv
from jet.filters import RelatedFieldAjaxListFilter


class DepartamentoAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'nombre')
    list_filter = ['codigo']
    search_fields = ['codigo', 'nombre']


class CiudadAdmin(admin.ModelAdmin):
    list_display = ('departamento', 'codigo', 'nombre')
    list_filter = ['departamento__nombre', 'nombre']
    search_fields = ['departamento__nombre', 'nombre', 'codigo']
    raw_id_fields = ('departamento',)


class MunicipioAdmin(admin.ModelAdmin):
    list_display = ('departamento', 'codigo', 'nombre')
    list_filter = ['departamento__nombre', 'nombre']
    search_fields = ['departamento__nombre', 'codigo', 'nombre']
    raw_id_fields = ('departamento',)


class PersonaAdmin(admin.ModelAdmin):
    list_display = (
    'identificacion', 'primer_nombre', 'segundo_nombre', 'primer_apellido', 'segundo_apellido', 'fecha_nacimiento',
    'tipo_de_sangre', 'sexo', 'telefono', 'direccion', 'correo_electronico', 'ciudad')
    list_filter = ['primer_nombre', 'primer_apellido']
    search_fields = ['identificacion', 'primer_nombre', 'primer_apellido']
    actions = [export_as_csv]
    raw_id_fields = ('ciudad','municipio')


class EpsAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'nombre')
    list_filter = ['nombre']
    search_fields = ['codigo', 'nombre']


class PacienteAdmin(admin.ModelAdmin):
    list_display = ('persona', 'codigo', 'eps', 'historia_clinica')
    list_filter = ['codigo', 'eps']
    search_fields = ['codigo', 'persona__identificacion', 'persona__primer_nombre']
    raw_id_fields = ('persona', 'historia_clinica', 'eps',)


class EspecialidadMedicaAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'nombre')
    list_filter = ['nombre']
    search_fields = ['codigo', 'nombre']


class MedicoAdmin(admin.ModelAdmin):
    list_display = ('persona', 'codigo', 'eps', 'especialidad')
    list_filter = ['persona__primer_apellido']
    search_fields = ['persona__identificacion', 'codigo', 'especialidad', 'eps']
    raw_id_fields = ('persona', 'eps', 'especialidad',)


class CitaAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'paciente', 'medico', 'especialidad', 'fecha', 'hora')
    list_filter = ['paciente__persona__primer_apellido']
    search_fields = ['paciente__persona__identificacion', 'codigo', 'medico', 'fecha', 'paciente']
    raw_id_fields = ('paciente', 'medico', 'especialidad',)


class TipoTratamientoAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'nombre', 'descripcion')
    search_fields = ['nombre']


class IncapacidadAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'fecha', 'dias')


class TipoExamenAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'nombre')
    list_filter = ['codigo']
    search_fields = ['nombre']


class ExamenAdmin(admin.ModelAdmin):
    list_display = (
    'tipo_examen', 'codigo', 'nombre', 'fecha_solicitud', 'fecha_aplicacion', 'observaciones', 'historia_clinica')
    list_filter = ['nombre', 'tipo_examen__nombre', 'fecha_solicitud']
    search_fields = ['nombre', 'fecha_solicitud', 'fecha_aplicacion', 'tipo_examen']
    raw_id_fields = ('tipo_examen', 'historia_clinica')


class TratamientoAdmin(admin.ModelAdmin):
    list_display = (
    'tipo_tratamiento', 'codigo', 'nombre', 'fecha_solicitud', 'fecha_inicio', 'fecha_finalizacion', 'observaciones',
    'historia_clinica', 'medico', 'incapacidad', 'precio')
    list_filter = ['nombre', 'fecha_solicitud', 'codigo']
    search_fields = ['tipo_tratamiento__nombre', 'medico__persona__identificacion', 'precio']
    raw_id_fields = ('tipo_tratamiento', 'historia_clinica', 'medico','incapacidad')


class ResultadosAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'fecha_entrega', 'descripcion', 'historia_clinica', 'tipo_examen')
    list_filter = ['fecha_entrega']
    search_fields = ['cdoigo', 'fecha_entrega']
    raw_id_fields = ('historia_clinica', 'tipo_examen')


class ClienteAdmin(admin.ModelAdmin):
    list_display = ('persona', 'codigo')
    list_filter = ['persona__primer_apellido']
    search_fields = ['codigo', 'cliente__persona__identificacion']
    raw_id_fields = ('persona',)


class CargoAdmin(admin.ModelAdmin):
    list_filter = ('nombre', 'codigo', 'descripcion')
    list_filter = ['nombre']
    search_fields = ['nombre', 'codigo']


class TipoEmpleadoAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'nombre', 'descripcion')
    list_filter = ['nombre']
    search_fields = ['codigo', 'nombre']


class HorarioAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'hora_inicio', 'hora_fin')
    list_filter = ['hora_inicio', 'hora_fin']
    search_fields = ['codigo', 'hora_inicio', 'hora_fin']


class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'nombre')


class EmpleadoAdmin(admin.ModelAdmin):
    list_display = ('persona', 'codigo', 'cargo', 'horario', 'tipo_empleado', 'usuario')
    list_filter = ['cargo__nombre', 'tipo_empleado__nombre', 'persona__primer_apellido']
    search_fields = ['codigo', 'tipo_empleado__nombre', 'cargo__nombre', 'persona__identificacion']
    raw_id_fields = ('persona', 'cargo', 'horario', 'tipo_empleado', 'usuario')


class NominaAdmin(admin.ModelAdmin):
    list_display = ('empleado', 'codigo', 'sueldo', 'rodamiento', 'prestamo', '_sueldofinal_')
    list_filter = ['sueldo', 'empleado__persona__primer_nombre']
    search_fields = ['codigo', 'sueldo', 'empleado__persona__identificacion']
    raw_id_fields = ('empleado',)


class PermisoAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'nombre', 'descripcion')
    list_filter = ['nombre']
    search_fields = ['codigo', 'nombre']


class TipoProductoAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'nombre')
    list_filter = ['nombre']
    search_fields = ['codigo', 'nombre']


class ProductoAdmin(admin.ModelAdmin):
    list_display = (
    'tipo_producto', 'codigo', 'nombre', 'fecha_vencimiento', 'precio_compra', 'precio_venta', 'cantidad')
    list_filter = ['tipo_producto__nombre']
    search_fields = ['codigo', 'tipo_producto__nombre', 'nombre', 'precio_venta']
    raw_id_fields = ('tipo_producto',)


class FacturaAdmin(admin.ModelAdmin):
    list_display = ('cliente', 'codigo', 'fecha_venta')
    list_filter = ['cliente__persona__primer_apellido']
    search_fields = ['codigo', 'fecha_venta', 'cliente__persona__identificacion']
    raw_id_fields = ('cliente',)


class ModoPagoAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'nombre', 'descripcion')
    search_fields = ['nombre']


class DetalleFacturaAdmin(admin.ModelAdmin):
    list_display = ('productos', 'codigo', 'cantidad', 'valor')
    list_filter = ['producto__nombre', 'codigo']
    search_fields = ['producto__nombre', 'codigo', 'valor']
    filter_horizontal = ('producto',)
    raw_id_fields = ('codigo',)


admin.site.register(Persona, PersonaAdmin)
admin.site.register(Medico, MedicoAdmin)
admin.site.register(ModoPago, ModoPagoAdmin)
admin.site.register(Paciente, PacienteAdmin)
admin.site.register(Cliente, ClienteAdmin)
admin.site.register(Empleado, EmpleadoAdmin)
admin.site.register(Nomina, NominaAdmin)
admin.site.register(Cita, CitaAdmin)
admin.site.register(Resultados, ResultadosAdmin)
admin.site.register(TipoTratamiento, TipoTratamientoAdmin)
admin.site.register(Tratamiento, TratamientoAdmin)
admin.site.register(Incapacidad, IncapacidadAdmin)
admin.site.register(TipoExamen, TipoExamenAdmin)
admin.site.register(Examen, ExamenAdmin)
admin.site.register(TipoEmpleado, TipoEmpleadoAdmin)
admin.site.register(Horario, HorarioAdmin)
admin.site.register(Usuario, UsuarioAdmin)
admin.site.register(Permiso, PermisoAdmin)
admin.site.register(PermisoXUsuario)
admin.site.register(TipoProducto, TipoProductoAdmin)
admin.site.register(Producto, ProductoAdmin)
admin.site.register(Factura, FacturaAdmin)
admin.site.register(DetalleFactura, DetalleFacturaAdmin)
admin.site.register(Ciudad, CiudadAdmin)
admin.site.register(Cargo, CargoAdmin)
admin.site.register(Departamento, DepartamentoAdmin)
admin.site.register(Municipio, MunicipioAdmin)
admin.site.register(EspecialidadMedica, EspecialidadMedicaAdmin)
admin.site.register(Eps, EpsAdmin)
admin.site.register(HistoriaClinica)
