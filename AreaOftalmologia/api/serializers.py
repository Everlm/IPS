from rest_framework import serializers
from AreaOftalmologia.models import *


class DepartamentoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Departamento
        fields = ('url', 'codigo', 'nombre',)


class CiudadSerializer(serializers.HyperlinkedModelSerializer):
    departamento = DepartamentoSerializer()

    class Meta:
        model = Ciudad
        fields = ('url', 'departamento', 'codigo', 'nombre',)


class SetPassword(serializers.Serializer):
    pasword1 = serializers.CharField(max_length=20)
    pasword2 = serializers.CharField(max_length=20)


class MunicipioSerializer(serializers.HyperlinkedModelSerializer):
    departamento = DepartamentoSerializer()

    class Meta:
        model = Municipio
        fields = ('url', 'departamento', 'codigo', 'nombre',)


class PersonaSerializer(serializers.HyperlinkedModelSerializer):
    ciudad = CiudadSerializer()

    class Meta:
        model = Persona
        fields = ('url', 'identificacion', 'primer_nombre', 'segundo_nombre',
                  'primer_apellido', 'segundo_apellido', 'fecha_nacimiento',
                  'tipo_de_sangre', 'sexo', 'telefono', 'direccion',
                  'correo_electronico', 'ciudad',)


class EpsSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Eps
        fields = ('url', 'codigo', 'nombre',)


class HistoriaClinicaSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = HistoriaClinica
        fields = ('url', 'codigo',)


class PacienteSerializer(serializers.HyperlinkedModelSerializer):
    persona = PersonaSerializer()
    eps = EpsSerializer()
    historia_clinica = HistoriaClinicaSerializer()

    class Meta:
        model = Paciente
        fields = ('url', 'persona', 'codigo', 'eps', 'historia_clinica',)


class EspecialidadMedicaSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = EspecialidadMedica
        fields = ('url', 'codigo', 'nombre',)


class MedicoSerializer(serializers.HyperlinkedModelSerializer):
    persona = PersonaSerializer()
    eps = EpsSerializer()
    especialidad = EspecialidadMedicaSerializer()

    class Meta:
        model = Medico
        fields = ('url', 'persona', 'codigo', 'eps', 'especialidad',)


class CitaSerializer(serializers.HyperlinkedModelSerializer):
    paciente = PacienteSerializer()
    medico = MedicoSerializer()
    especialidad = EspecialidadMedicaSerializer()

    class Meta:
        model = Cita
        fields = ('url', 'codigo', 'paciente', 'medico', 'especialidad',
                  'fecha', 'hora',)


class TipoTratamientoSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = TipoTratamiento
        fields = ('url', 'nombre', 'descripcion',)


class IncapacidadSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Incapacidad
        fields = ('url', 'codigo', 'fecha', 'dias',)


class TipoExamenSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = TipoExamen
        fields = ('url', 'codigo', 'nombre',)


class ExamenSerializer(serializers.HyperlinkedModelSerializer):
    tipo_examen = TipoExamenSerializer()
    historia_clinica = HistoriaClinicaSerializer()

    class Meta:
        model = Examen
        fields = ('url', 'tipo_examen', 'codigo', 'nombre', 'fecha_solicitud',
                  'fecha_aplicacion', 'observaciones', 'historia_clinica',)


class TratamientoSerializer(serializers.HyperlinkedModelSerializer):
    tipo_tratamiento = TipoTratamientoSerializer()
    historia_clinica = HistoriaClinicaSerializer()
    medico = MedicoSerializer()
    incapacidad = IncapacidadSerializer()

    class Meta:
        model = Tratamiento
        fields = ('url', 'tipo_tratamiento', 'codigo', 'nombre', 'fecha_solicitud',
                  'fecha_inicio', 'fecha_finalizacion', 'observaciones', 'historia_clinica',
                  'medico', 'incapacidad', 'precio',)


class ResultadosSerializer(serializers.HyperlinkedModelSerializer):
    historia_clinica = HistoriaClinicaSerializer()
    ipo_examen = TipoExamenSerializer()

    class Meta:
        model = Resultados
        fields = ('url', 'codigo', 'fecha_entrega', 'descripcion', 'historia_clinica',
                  'tipo_examen',)


class ClienteSerializer(serializers.HyperlinkedModelSerializer):
    persona = PacienteSerializer()

    class Meta:
        model = Cliente
        fields = ('url', 'persona', 'codigo',)


class CargoSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Cargo
        fields = ('url', 'codigo', 'nombre', 'descripcion',)


class TipoEmpleadoSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = TipoEmpleado
        fields = ('url', 'codigo', 'nombre', 'descripcion',)


class HorarioSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Horario
        fields = ('url', 'codigo', 'dia', 'hora_inicio', 'hora_fin',)


class UsuarioSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Usuario
        fields = ('url', 'codigo', 'nombre',)


class EmpleadoSerializer(serializers.HyperlinkedModelSerializer):
    persona = PersonaSerializer()
    cargo = CargoSerializer()
    horario = HorarioSerializer()
    tipo_empleado = TipoEmpleadoSerializer()
    usuario = UsuarioSerializer()

    class Meta:
        model = Empleado
        fields = ('url', 'persona', 'codigo', 'cargo', 'horario', 'tipo_empleado', 'usuario',)


class NominaSerializer(serializers.HyperlinkedModelSerializer):
    empleado = EmpleadoSerializer()

    class Meta:
        model = Nomina
        fields = ('url', 'empleado', 'codigo', 'sueldo', 'rodamiento', 'prestamo',)


class PermisoSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Permiso
        fields = ('url', 'codigo', 'nombre', 'descripcion',)


class TipoProductoSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = TipoProducto
        fields = ('url', 'codigo', 'nombre',)


class ProductoSerializer(serializers.HyperlinkedModelSerializer):
    tipo_producto = TipoProductoSerializer

    class Meta:
        model = Producto
        fields = ('url', 'tipo_producto', 'codigo', 'nombre', 'fecha_vencimiento', 'precio_compra',
                  'precio_venta', 'cantidad',)


class FacturaSerializer(serializers.HyperlinkedModelSerializer):
    cliente = ClienteSerializer()

    class Meta:
        model = Factura
        fields = ('url', 'codigo', 'cliente', 'fecha_venta',)


class ModoPagoSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = ModoPago
        fields = ('url', 'codigo', 'nombre', 'descripcion',)


class DetalleFacturaSerializer(serializers.HyperlinkedModelSerializer):
    producto = ProductoSerializer()
    codigo = FacturaSerializer()

    class Meta:
        model = Factura
        fields = ('url', 'producto', 'codigo',)