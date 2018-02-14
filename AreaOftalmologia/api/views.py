from rest_framework import viewsets
from rest_framework import permissions
from rest_framework import filters
from AreaOftalmologia.api.serializers import *
from AreaOftalmologia.models import *


class DepartamentoViewSet(viewsets.ModelViewSet):
    queryset = Departamento.objects.all()
    serializer_class = DepartamentoSerializer
    permission_classes = (permissions.IsAuthenticated,)


class CiudadViewSet(viewsets.ModelViewSet):
    queryset = Ciudad.objects.all()
    serializer_class = CiudadSerializer
    permission_classes = (permissions.IsAuthenticated,)
    filter_backends = (filters.DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    search_fields = ('departamento__codigo', 'departamento__nombre')
    ordering_fields = ('nombre')
    #filter_class = CiudadFilter

    def list(self, request, *args, **kwargs):
        print(request.user)
        return super(CiudadViewSet, self).list(request, *args, **kwargs)


class MunicipioViewSet(viewsets.ModelViewSet):
    queryset = Municipio.objects.all()
    serializer_class = MunicipioSerializer
    permission_classes = (permissions.IsAuthenticated,)


class PersonaViewSet(viewsets.ModelViewSet):
    queryset = Persona.objects.all()
    serializer_class = PersonaSerializer
    permission_classes = (permissions.IsAuthenticated,)
    filter_backends = (filters.DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    search_fields = ('identificacion', 'primer_apellido')
    ordering_fields = ('nombre')


class EpsViewSet(viewsets.ModelViewSet):
    queryset = Eps.objects.all()
    serializer_class = EpsSerializer
    permission_classes = (permissions.IsAuthenticated,)
    filter_backends = (filters.DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)


class HistoriaClinicaViewSet(viewsets.ModelViewSet):
    queryset = HistoriaClinica.objects.all()
    serializer_class = HistoriaClinicaSerializer
    permission_classes = (permissions.IsAuthenticated,)
    filter_backends = (filters.DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)


class PacienteViewSet(viewsets.ModelViewSet):
    queryset = Paciente.objects.all()
    serializer_class = PacienteSerializer
    permission_classes = (permissions.IsAuthenticated,)
    filter_backends = (filters.DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)


class EspecialidadMedicaViewSet(viewsets.ModelViewSet):
    queryset = EspecialidadMedica.objects.all()
    serializer_class = EspecialidadMedicaSerializer
    permission_classes = (permissions.IsAuthenticated,)
    filter_backends = (filters.DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)


class MedicoViewSet(viewsets.ModelViewSet):
    queryset = Medico.objects.all()
    serializer_class = MedicoSerializer
    permission_classes = (permissions.IsAuthenticated,)
    filter_backends = (filters.DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)


class CitaViewSet(viewsets.ModelViewSet):
    queryset = Cita.objects.all()
    serializer_class = CiudadSerializer
    permission_classes = (permissions.IsAuthenticated,)
    filter_backends = (filters.DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)


class TipoTratamientoViewSet(viewsets.ModelViewSet):
    queryset = TipoTratamiento.objects.all()
    serializer_class = TipoTratamientoSerializer
    permission_classes = (permissions.IsAuthenticated,)
    filter_backends = (filters.DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)


class IncapacidadViewSet(viewsets.ModelViewSet):
    queryset = Incapacidad.objects.all()
    serializer_class = IncapacidadSerializer
    permission_classes = (permissions.IsAuthenticated,)
    filter_backends = (filters.DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)


class TipoExamenViewSet(viewsets.ModelViewSet):
    queryset = TipoTratamiento.objects.all()
    serializer_class = TipoExamenSerializer
    permission_classes = (permissions.IsAuthenticated,)
    filter_backends = (filters.DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)


class ExamenViewSet(viewsets.ModelViewSet):
    queryset = Examen.objects.all()
    serializer_class = ExamenSerializer
    permission_classes = (permissions.IsAuthenticated,)
    filter_backends = (filters.DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)


class TratamientoViewSet(viewsets.ModelViewSet):
    queryset = Tratamiento.objects.all()
    serializer_class = TratamientoSerializer
    permission_classes = (permissions.IsAuthenticated,)
    filter_backends = (filters.DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)


class ResultadosViewSet(viewsets.ModelViewSet):
    queryset = Resultados.objects.all()
    serializer_class = ResultadosSerializer
    permission_classes = (permissions.IsAuthenticated,)
    filter_backends = (filters.DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)


class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
    permission_classes = (permissions.IsAuthenticated,)
    filter_backends = (filters.DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)


class CargoViewSet(viewsets.ModelViewSet):
    queryset = Cargo.objects.all()
    serializer_class = CargoSerializer
    permission_classes = (permissions.IsAuthenticated,)
    filter_backends = (filters.DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)


class TipoEmpleadoViewSet(viewsets.ModelViewSet):
    queryset = TipoEmpleado.objects.all()
    serializer_class = TipoEmpleadoSerializer
    permission_classes = (permissions.IsAuthenticated,)
    filter_backends = (filters.DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)


class HorarioViewSet(viewsets.ModelViewSet):
    queryset = Horario.objects.all()
    serializer_class = HorarioSerializer
    permission_classes = (permissions.IsAuthenticated,)
    filter_backends = (filters.DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)


class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
    permission_classes = (permissions.IsAuthenticated,)
    filter_backends = (filters.DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)


class EmpleadoViewSet(viewsets.ModelViewSet):
    queryset = Empleado.objects.all()
    serializer_class = EmpleadoSerializer
    permission_classes = (permissions.IsAuthenticated,)
    filter_backends = (filters.DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)


class NominaViewSet(viewsets.ModelViewSet):
    queryset = Nomina.objects.all()
    serializer_class = NominaSerializer
    permission_classes = (permissions.IsAuthenticated,)
    filter_backends = (filters.DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)


class PermisoViewSet(viewsets.ModelViewSet):
    queryset = Permiso.objects.all()
    serializer_class = PermisoSerializer
    permission_classes = (permissions.IsAuthenticated,)
    filter_backends = (filters.DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)


class TipoProductoViewSet(viewsets.ModelViewSet):
    queryset = TipoProducto.objects.all()
    serializer_class = TipoProductoSerializer
    permission_classes = (permissions.IsAuthenticated,)
    filter_backends = (filters.DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)


class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer
    permission_classes = (permissions.IsAuthenticated,)
    filter_backends = (filters.DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)


class FacturaViewSet(viewsets.ModelViewSet):
    queryset = Factura.objects.all()
    serializer_class = FacturaSerializer
    permission_classes = (permissions.IsAuthenticated,)
    filter_backends = (filters.DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)


class ModoPagoViewSet(viewsets.ModelViewSet):
    queryset = ModoPago.objects.all()
    serializer_class = ModoPagoSerializer
    permission_classes = (permissions.IsAuthenticated,)
    filter_backends = (filters.DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)


class DetalleFacturaViewSet(viewsets.ModelViewSet):
    queryset = DetalleFactura.objects.all()
    serializer_class = DetalleFacturaSerializer
    permission_classes = (permissions.IsAuthenticated,)
    filter_backends = (filters.DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
