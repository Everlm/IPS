from django.test import TestCase
from AreaOftalmologia.models import *


class DepartamentoTestCase(TestCase):
    # Le asignamos parametros a la variable creada
    def setUp(self):
        self.departamento = Departamento.objects.create(
            codigo="01",
            nombre="Cesar",
        )

    # testiamos el metodo
    def test___str__(self):
        self.assertEquals(self.departamento.__str__(), "Cesar")


class CiudadTestCase(TestCase):
    def setUp(self):
        departamento = Departamento.objects.create(
            codigo="01",
            nombre="Cesar"
        )
        self.ciudad = Ciudad.objects.create(
            departamento=departamento,
            codigo="01",
            nombre="Valledupar",
        )

    def test___str__(self):
        self.assertEquals(self.ciudad.__str__(), "Valledupar")


class MunicipioTestCase(TestCase):
    def setUp(self):
        departamento = Departamento.objects.create(
            codigo="01",
            nombre="Cesar"
        )

        self.municipio = Municipio.objects.create(
            departamento=departamento,
            codigo="01",
            nombre="La paz",
        )

    def test___str__(self):
        self.assertEquals(self.municipio.__str__(), "La paz")


class PersonaTestCase(TestCase):
    def setUp(self):
        departamento = Departamento.objects.create(
            codigo="01",
            nombre="Cesar"
        )

        ciudad = Ciudad.objects.create(
            departamento=departamento,
            codigo="01",
            nombre="Valledupar"
        )

        self.persona = Persona.objects.create(
            ciudad=ciudad,
            fecha_nacimiento="1993-02-03",
            identificacion="10",
            primer_nombre="Ever",
            primer_apellido="Machado",
        )

    def test___str__(self):
        self.assertEquals(self.persona.__str__(), "10" + '  ' + "Ever" + '  ' + "Machado")


class EpsTestCase(TestCase):
    def setUp(self):
        self.eps = Eps.objects.create(
            codigo="01",
            nombre="Nueva eps"
        )

    def test___str__(self):
        self.assertEquals(self.eps.__str__(), "Nueva eps")


class HistoriaClinicaTestCase(TestCase):
    def setUp(self):
        self.hisotira_clinica = HistoriaClinica.objects.create(
            codigo="01"
        )

    def test___str__(self):
        self.assertEquals(self.hisotira_clinica.__str__(), "01")


class PacienteTestCase(TestCase):
    def setUp(self):
        departamento = Departamento.objects.create(
            codigo="01",
            nombre="Cesar"
        )

        ciudad = Ciudad.objects.create(
            departamento=departamento,
            codigo="01",
            nombre="Valledupar"
        )

        persona = Persona.objects.create(
            ciudad=ciudad,
            fecha_nacimiento="1993-02-03",
            identificacion="10",
            primer_nombre="Ever",
            primer_apellido="Machado"
        )

        eps = Eps.objects.create(
            codigo="01",
            nombre="Nueva eps"
        )

        historia_clinica = HistoriaClinica.objects.create(
            codigo="01"
        )

        self.paciente = Paciente.objects.create(
            persona=persona,
            codigo="01",
            eps=eps,
            historia_clinica=historia_clinica
        )

    def test___str__(self):
        self.assertEquals(self.paciente.__str__(), "10" + ' ' + "Ever" + ' ' + "Machado")


class EspecialidadMedicaTestCase(TestCase):
    def setUp(self):
        self.especialidad_medica = EspecialidadMedica.objects.create(
            codigo="01",
            nombre="Cirujano"
        )

    def test___str__(self):
        self.assertEquals(self.especialidad_medica.__str__(), "Cirujano")


class MedicoTestCase(TestCase):
    def setUp(self):
        departamento = Departamento.objects.create(
            codigo="01",
            nombre="Cesar"
        )

        ciudad = Ciudad.objects.create(
            departamento=departamento,
            codigo="01",
            nombre="Valledupar"
        )

        persona = Persona.objects.create(
            ciudad=ciudad,
            fecha_nacimiento="1993-02-03",
            identificacion="10",
            primer_nombre="Ever",
            primer_apellido="Machado"
        )

        eps = Eps.objects.create(
            codigo="01",
            nombre="Nueva eps"
        )

        especialidad_medica = EspecialidadMedica.objects.create(
            codigo="01",
            nombre="Cirujano"
        )

        self.medico = Medico.objects.create(
            persona=persona,
            codigo="01",
            eps=eps,
            especialidad=especialidad_medica
        )

    def test__str__(self):
        self.assertEquals(self.medico.__str__(), "10" + ' ' + "Ever" + ' ' + "Machado")


class CitaTestCase(TestCase):
    def setUp(self):
        departamento = Departamento.objects.create(
            codigo="01",
            nombre="Cesar"
        )

        ciudad = Ciudad.objects.create(
            departamento=departamento,
            codigo="01",
            nombre="Valledupar"
        )

        persona = Persona.objects.create(
            ciudad=ciudad,
            fecha_nacimiento="1993-02-03",
            identificacion="10",
            primer_nombre="Ever",
            primer_apellido="Machado"
        )

        especialidad_medica = EspecialidadMedica.objects.create(
            codigo="01",
            nombre="Cirujano"
        )

        eps = Eps.objects.create(
            codigo="01",
            nombre="Nueva eps"
        )

        medico = Medico.objects.create(
            persona=persona,
            codigo="01",
            eps=eps,
            especialidad=especialidad_medica
        )

        historia_clinica = HistoriaClinica.objects.create(
            codigo="01"
        )
        paciente = Paciente.objects.create(
            persona=persona,
            codigo="01",
            eps=eps,
            historia_clinica=historia_clinica
        )

        self.cita = Cita.objects.create(
            codigo="01",
            paciente=paciente,
            medico=medico,
            especialidad=especialidad_medica,
            fecha="2016-03-16",
            hora="15:00"
        )

    def test___str__(self):
        self.assertEquals(self.cita.__str__(), "10")


class TipoTratamientoTestCase(TestCase):
    def setUp(self):
        self.tipo_tratamiento = TipoTratamiento.objects.create(
            codigo="01",
            nombre="lente intraocular o LIO",
            descripcion=""
        )

    def test___str__(self):
        self.assertEquals(self.tipo_tratamiento.__str__(), "01")


class IncapacidadTestCase(TestCase):
    def setUp(self):
        self.incapacidad = Incapacidad.objects.create(
            codigo="01",
            fecha="2016-03-10",
            dias="03"
        )

    def test___str__(self):
        self.assertEquals(self.incapacidad.__str__(), "01")


class TipoExamenTestCase(TestCase):
    def setUp(self):
        self.tipo_examen = TipoExamen.objects.create(
            codigo="01",
            nombre="Examen completo"
        )

    def test__str__(self):
        self.assertEquals(self.tipo_examen.__str__(), "Examen completo")


class ExamenTestCase(TestCase):
    def setUp(self):
        tipo_de_examen = TipoExamen.objects.create(
            codigo="01",
            nombre="Examen completo"
        )

        historia_clinica = HistoriaClinica.objects.create(
            codigo="01"
        )

        self.examen = Examen.objects.create(
            tipo_examen=tipo_de_examen,
            codigo="01",
            nombre="Examen completo con dilatacion de pupilas",
            fecha_solicitud="2016-03-14",
            fecha_aplicacion="2016-03-20",
            observaciones="",
            historia_clinica=historia_clinica
        )

    def test__str__(self):
        self.assertEquals(self.examen.__str__(), "01")


class TratamientoTestCase(TestCase):
    def setUp(self):
        tipo_de_tratamiento = TipoTratamiento.objects.create(
            codigo="01",
            nombre=""
                   ""
                   "",
            descripcion=""
        )

        historia_clinica = HistoriaClinica.objects.create(
            codigo="01"
        )

        incapacidad = Incapacidad.objects.create(
            codigo="01",
            fecha="2016-03-10",
            dias="03"
        )

        departmento = Departamento.objects.create(
            codigo="01",
            nombre="Cesar"
        )

        ciudad = Ciudad.objects.create(
            departamento=departmento,
            codigo="01",
            nombre="Valledupar"
        )

        persona = Persona.objects.create(
            ciudad=ciudad,
            fecha_nacimiento="1993-02-03",
            identificacion="10",
            primer_nombre="Ever",
            primer_apellido="Machado"
        )

        especialidad_medica = EspecialidadMedica.objects.create(
            codigo="01",
            nombre="Cirujano"
        )

        eps = Eps.objects.create(
            codigo="01",
            nombre="Nueva eps"
        )

        medico = Medico.objects.create(
            persona=persona,
            codigo="01",
            eps=eps,
            especialidad=especialidad_medica
        )

        self.tratamiento = Tratamiento.objects.create(
            tipo_tratamiento=tipo_de_tratamiento,
            codigo="01",
            nombre="Melanoma ocular",
            fecha_solicitud="2016-03-17",
            fecha_inicio="2016-03-24",
            fecha_finalizacion="2016-04-10",
            observaciones="paciente requerido",
            historia_clinica=historia_clinica,
            medico=medico,
            incapacidad=incapacidad,
            precio="340.000"
        )

    def test___str__(self):
        self.assertEquals(self.tratamiento.__str__(), "Melanoma ocular")


class ResultadosTestCase(TestCase):
    def setUp(self):
        historia_clinica = HistoriaClinica.objects.create(
            codigo="01"
        )

        tipo_de_examen = TipoExamen.objects.create(
            codigo="01",
            nombre="Examen completo"
        )

        self.resultados = Resultados.objects.create(
            codigo="01",
            fecha_entrega="2016-03-21",
            descripcion="presenta anomalia ocular",
            historia_clinica=historia_clinica,
            tipo_examen=tipo_de_examen
        )

    def test__str__(self):
        self.assertEquals(self.resultados.__str__(), "01")


class ClienteTestCase(TestCase):
    def setUp(self):
        departamento = Departamento.objects.create(
            codigo="01",
            nombre="Cesar"
        )

        ciudad = Ciudad.objects.create(
            departamento=departamento,
            codigo="01",
            nombre="Valledupar"
        )

        persona = Persona.objects.create(
            ciudad=ciudad,
            fecha_nacimiento="1993-02-03",
            identificacion="10",
            primer_nombre="Ever",
            primer_apellido="Machado"
        )

        self.cliente = Cliente.objects.create(
            persona=persona,
            codigo="01"
        )

    def test___str__(self):
        self.assertEquals(self.cliente.__str__(), "10" + ' ' + "Ever" + ' ' + "Machado")


class CargoTestCase(TestCase):
    def setUp(self):
        self.cargo = Cargo.objects.create(
            codigo="01",
            nombre="Jefe de sistemas",
            descripcion="encargado del area de sistemas"
        )

    def test___str__(self):
        self.assertEquals(self.cargo.__str__(), "Jefe de sistemas")


class TipoEmpleadoTestCase(TestCase):
    def setUp(self):
        self.tipoempelado = TipoEmpleado.objects.create(
            codigo="01",
            nombre="indefinido",
            descripcion=""
        )

    def test___str__(self):
        self.assertEquals(self.tipoempelado.__str__(), "indefinido")


class HorarioTestCase(TestCase):
    def setUp(self):
        self.horario = Horario.objects.create(
            dia="lunes",
            codigo="01",
            hora_inicio="8:00",
            hora_fin="16:00",
        )

    def test___str__(self):
        self.assertEquals(self.horario.__str__(), "01")


class UsuarioTestCase(TestCase):
    def setUp(self):
        self.usuario = Usuario.objects.create(
            codigo="01",
            nombre="super usuario"
        )

    def test___str__(self):
        self.assertEquals(self.usuario.__str__(), "super usuario")


class EmpleadoTestCase(TestCase):
    def setUp(self):
        departamento = Departamento.objects.create(
            codigo="01",
            nombre="Cesar"
        )

        ciudad = Ciudad.objects.create(
            departamento=departamento,
            codigo="01",
            nombre="Valledupar"
        )

        persona = Persona.objects.create(
            ciudad=ciudad,
            fecha_nacimiento="1993-02-03",
            identificacion="10",
            primer_nombre="Ever",
            primer_apellido="Machado"
        )

        usuario = Usuario.objects.create(
            codigo="01",
            nombre="super usuario"
        )

        cargo = Cargo.objects.create(
            codigo="01",
            nombre="Jefe de sistemas",
            descripcion="encargado del area de sistemas"
        )

        horario = Horario.objects.create(
            dia="lunes",
            codigo="01",
            hora_inicio="8:00",
            hora_fin="16:00",
        )

        tipo_de_empelado = TipoEmpleado.objects.create(
            codigo="01",
            nombre="indefinido",
            descripcion=""
        )

        self.empleado = Empleado.objects.create(
            persona=persona,
            codigo="01",
            cargo=cargo,
            horario=horario,
            tipo_empleado=tipo_de_empelado,
            usuario=usuario
        )

    def test__str__(self):
        self.assertEquals(self.empleado.__str__(), "01")


class NominaTestCase(TestCase):
    def setUp(self):
        departamento = Departamento.objects.create(
            codigo="01",
            nombre="Cesar"
        )

        ciudad = Ciudad.objects.create(
            departamento=departamento,
            codigo="01",
            nombre="Valledupar"
        )

        persona = Persona.objects.create(
            ciudad=ciudad,
            fecha_nacimiento="1993-02-03",
            identificacion="10",
            primer_nombre="Ever",
            primer_apellido="Machado"
        )

        usuario = Usuario.objects.create(
            codigo="01",
            nombre="super usuario"
        )

        cargo = Cargo.objects.create(
            codigo="01",
            nombre="Jefe de sistemas",
            descripcion="encargado del area de sistemas"
        )

        horario = Horario.objects.create(
            dia="lunes",
            codigo="01",
            hora_inicio="8:00",
            hora_fin="16:00",
        )

        tipo_de_empelado = TipoEmpleado.objects.create(
            codigo="01",
            nombre="indefinido",
            descripcion=""
        )

        empleado = Empleado.objects.create(
            persona=persona,
            codigo="01",
            cargo=cargo,
            horario=horario,
            tipo_empleado=tipo_de_empelado,
            usuario=usuario
        )

        self.nomina = Nomina.objects.create(
            empleado=empleado,
            codigo="01",
            sueldo="500.000",
            rodamiento="100.000",
            prestamo="0"
        )

    def test___str__(self):
        self.assertEquals(self.nomina.__str__(), "01")


class PermisoTestCase(TestCase):
    def setUp(self):
        self.permiso = Permiso.objects.create(
            codigo="01",
            nombre="Alfa",
            descripcion=""
        )

    def test___str__(self):
        self.assertEquals(self.permiso.__str__(), "Alfa")


class TipoProductoTestCase(TestCase):
    def setUp(self):
        self.tipoproducto = TipoProducto.objects.create(
            codigo="01",
            nombre="Analgesicos"
        )

    def test___str__(self):
        self.assertEquals(self.tipoproducto.__str__(), "Analgesicos")


class ProductoTestCase(TestCase):
    def setUp(self):
        tipoproducto = TipoProducto.objects.create(
            codigo="01",
            nombre="Analgesicos"
        )

        self.producto = Producto.objects.create(
            tipo_producto=tipoproducto,
            codigo="01",
            nombre="gotas oculares",
            fecha_vencimiento="2017-03-10",
            precio_compra="15.000",
            precio_venta="40.000",
            cantidad="100"
        )

    def test___str__(self):
        self.assertEquals(self.producto.__str__(), "gotas oculares")


class FacturaTestCase(TestCase):
    def setUp(self):
        departamento = Departamento.objects.create(
            codigo="01",
            nombre="Cesar"
        )

        ciudad = Ciudad.objects.create(
            departamento=departamento,
            codigo="01",
            nombre="Valledupar"
        )

        persona = Persona.objects.create(
            ciudad=ciudad,
            fecha_nacimiento="1993-02-03",
            identificacion="10",
            primer_nombre="Ever",
            primer_apellido="Machado"
        )

        cliente = Cliente.objects.create(
            persona=persona,
            codigo="01"
        )

        self.factura = Factura.objects.create(
            cliente=cliente,
            codigo="01",
            fecha_venta="2016-03-17"
        )

    def test___str__(self):
        self.assertEquals(self.factura.__str__(), "01")


class ModoPagoTestCase(TestCase):
    def setUp(self):
        self.modopago = ModoPago.objects.create(
            codigo="01",
            nombre="tarjeta de credito",
            descripcion=""
        )

    def test___str__(self):
        self.assertEquals(self.modopago.__str__(), "tarjeta de credito")


