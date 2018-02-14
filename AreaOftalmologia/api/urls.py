from django.conf.urls import url, patterns, include
from  AreaOftalmologia.models import Ciudad
from rest_framework import routers
from AreaOftalmologia.api.views import *

router = routers.DefaultRouter()
router.register(r'departamentos', DepartamentoViewSet)
router.register(r'ciudades', CiudadViewSet)
router.register(r'municipios', MunicipioViewSet)
router.register(r'personas', PersonaViewSet)
router.register(r'eps', EpsViewSet)
router.register(r'historias_clinicas', HistoriaClinicaViewSet)
router.register(r'pacientes', PacienteViewSet)
router.register(r'especialidad_medica', EspecialidadMedicaViewSet)
router.register(r'medicos', MedicoViewSet)
router.register(r'citas', CitaViewSet)
router.register(r'tipo_tratamiento', TipoTratamientoViewSet)
router.register(r'incapacidades', IncapacidadViewSet)
router.register(r'tipo_examen', TipoExamenViewSet)
router.register(r'examenes', ExamenViewSet)
router.register(r'tratamientos', TratamientoViewSet)
router.register(r'resultados', ResultadosViewSet)
router.register(r'clientes', ClienteViewSet)
router.register(r'cargos', CargoViewSet)
router.register(r'tipo_empleado', TipoEmpleadoViewSet)
router.register(r'horarios', HorarioViewSet)
router.register(r'usuarios', UsuarioViewSet)
router.register(r'empleados', EmpleadoViewSet)
router.register(r'nominas', NominaViewSet)
router.register(r'permisos', PermisoViewSet)
router.register(r'tipo_producto', TipoProductoViewSet)
router.register(r'productos', ProductoViewSet)
router.register(r'facturas', FacturaViewSet)
router.register(r'modo_pago', ModoPagoViewSet)
router.register(r'detalle_facturas', DetalleFacturaViewSet)





urlpatterns = patterns('',

    url(r'^api/', include(router.urls)),

)
