from datetime import datetime
from django.db import models
from django.core.validators import RegexValidator


class Departamento(models.Model):
    codigo = models.CharField(max_length=10, primary_key=True)
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = 'Departamentos'


class Ciudad(models.Model):
    departamento = models.ForeignKey(Departamento)
    codigo = models.CharField(max_length=10, primary_key=True)
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

    class Meta:
        # nombre en plural del modelo en el admin
        verbose_name_plural = 'Ciudades'


class Municipio(models.Model):
    departamento = models.ForeignKey(Departamento)
    codigo = models.CharField(max_length=10, primary_key=True)
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = 'Municipios'


class Persona(models.Model):
    Generos = (
        ('Masculino', 'Masculino'),
        ('Femenino', 'Femenino'),
    )
    identificacion = models.CharField(max_length=12, primary_key=True, help_text='introduce cedula')
    primer_nombre = models.CharField(max_length=50)
    segundo_nombre = models.CharField(max_length=50, blank=True)
    primer_apellido = models.CharField(max_length=50)
    segundo_apellido = models.CharField(max_length=50)
    fecha_nacimiento = models.DateField()
    tipo_de_sangre = models.CharField(max_length=4)
    sexo = models.CharField(choices=Generos, max_length=10)
    telefono = models.IntegerField(null=True, blank=True)
    direccion = models.CharField(max_length=50)
    correo_electronico = models.EmailField(max_length=50, blank=True)
    ciudad = models.ForeignKey(Ciudad, blank=True)
    municipio = models.ForeignKey(Municipio, blank=True, null=True, default="no tiene")

    def __str__(self):
        return self.identificacion + '  ' + self.primer_nombre + '  ' + self.primer_apellido


    def validacion_fecha(self):
        fecha_actual = datetime.now()
        if self.fecha_nacimiento > fecha_actual:
            print('La fehca no puede ser mayor a la fecha actual')

    class Meta:
        verbose_name_plural = 'Personas'


class Eps(models.Model):
    codigo = models.CharField(max_length=10, primary_key=True)
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = 'EPS'


class HistoriaClinica(models.Model):
    codigo = models.CharField(max_length=10, primary_key=True)

    def __str__(self):
        return self.codigo

    class Meta:
        verbose_name_plural = 'Historias Clinicas'


class Paciente(models.Model):
    persona = models.ForeignKey(Persona)
    codigo = models.CharField(max_length=12, primary_key=True)
    eps = models.ForeignKey(Eps)
    historia_clinica = models.ForeignKey(HistoriaClinica)

    def __str__(self):
        return self.persona.identificacion + ' ' + self.persona.primer_nombre + ' ' + \
               self.persona.primer_apellido

    class Meta:
        verbose_name_plural = 'Pacientes'


class EspecialidadMedica(models.Model):
    codigo = models.CharField(max_length=10, primary_key=True)
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = 'Especialidad medica'


class Medico(models.Model):
    persona = models.ForeignKey(Persona)
    codigo = models.CharField(max_length=10, primary_key=True)
    eps = models.ForeignKey(Eps)
    especialidad = models.ForeignKey(EspecialidadMedica)

    def __str__(self):
        return self.persona.identificacion + ' ' + self.persona.primer_nombre + ' ' + \
               self.persona.primer_apellido

    class Meta:
        verbose_name_plural = 'Medicos'


class Cita(models.Model):
    codigo = models.CharField(max_length=10, primary_key=True)
    paciente = models.ForeignKey(Paciente)
    medico = models.ForeignKey(Medico)
    especialidad = models.ForeignKey(EspecialidadMedica)
    fecha = models.DateField()
    hora = models.TimeField()

    def __str__(self):
        return self.paciente.persona.identificacion

    class Meta:
        verbose_name_plural = 'Citas'


class TipoTratamiento(models.Model):
    codigo = models.CharField(max_length=10, primary_key=True)
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField(max_length=140)


    def __str__(self):
        return self.codigo

    class Meta:
        verbose_name_plural = 'Tipos de tratamientos'


class Incapacidad(models.Model):
    codigo = models.CharField(max_length=10, primary_key=True)
    fecha = models.DateTimeField()
    dias = models.CharField(max_length=10)

    def __str__(self):
        return self.codigo

    class Meta:
        verbose_name_plural = 'Incapacidades'


class TipoExamen(models.Model):
    codigo = models.CharField(max_length=10, primary_key=True)
    nombre = models.CharField(max_length=140)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = 'Tipos de examenes'


class Examen(models.Model):
    tipo_examen = models.ForeignKey(TipoExamen)
    codigo = models.CharField(max_length=10, primary_key=True)
    nombre = models.CharField(max_length=50)
    fecha_solicitud = models.DateTimeField()
    fecha_aplicacion = models.DateTimeField(auto_now_add=True)
    observaciones = models.TextField(max_length=140)
    historia_clinica = models.ForeignKey(HistoriaClinica)

    def __str__(self):
        return self.codigo

    class Meta:
        verbose_name_plural = 'Examenes'


class Tratamiento(models.Model):
    tipo_tratamiento = models.ForeignKey(TipoTratamiento)
    codigo = models.CharField(max_length=10, primary_key=True)
    nombre = models.CharField(max_length=50)
    fecha_solicitud = models.DateField(auto_now=True)
    fecha_inicio = models.DateField()
    fecha_finalizacion = models.DateField()
    observaciones = models.TextField(max_length=140)
    historia_clinica = models.ForeignKey(HistoriaClinica)
    medico = models.ForeignKey(Medico)
    incapacidad = models.ForeignKey(Incapacidad)
    precio = models.FloatField()

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = 'Tratamientos'


class Resultados(models.Model):
    codigo = models.CharField(max_length=10)
    fecha_entrega = models.DateTimeField(auto_now_add=True)
    descripcion = models.TextField(max_length=140)
    historia_clinica = models.ForeignKey(HistoriaClinica)
    tipo_examen = models.ForeignKey(TipoExamen)

    def __str__(self):
        return self.codigo

    class Meta:
        verbose_name_plural = 'Resultados de examenes'


class Cliente(models.Model):
    persona = models.ForeignKey(Persona)
    codigo = models.CharField(max_length=10, primary_key=True)

    def __str__(self):
        return self.persona.identificacion + ' ' + self.persona.primer_nombre + ' ' + \
               self.persona.primer_apellido

    class Meta:
        verbose_name_plural = 'Clientes'


class Cargo(models.Model):
    codigo = models.CharField(max_length=10, primary_key=True)
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField(max_length=140)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = 'Cargos'


class TipoEmpleado(models.Model):
    codigo = models.CharField(max_length=10, primary_key=True)
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField(max_length=140)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = 'Tipos de empleados'


class Horario(models.Model):
    Dias = (
        ('Lunes a Sabado', 'Lunes a Sabado'),
        ('Lunes a Viernes', 'Lunes a Viernes'),
        ('Lunes', 'Lunes'),
        ('Martes', 'Martes'),
        ('Miercoles', 'Miercoles'),
        ('Jueves', 'Jueves'),
        ('Viernes', 'viernes'),
        ('Sabado', 'Sabado'),
    )
    codigo = models.CharField(max_length=10, primary_key=True)
    dia = models.CharField(choices=Dias, max_length=20)
    hora_inicio = models.TimeField()
    hora_fin = models.TimeField()

    def __str__(self):
        return self.codigo

    class Meta:
        verbose_name_plural = 'Horarios'


class Usuario(models.Model):
    codigo = models.CharField(max_length=10, primary_key=True)
    nombre = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = 'Usuarios'


class Empleado(models.Model):
    persona = models.ForeignKey(Persona)
    codigo = models.CharField(max_length=10, primary_key=True)
    cargo = models.ForeignKey(Cargo)
    horario = models.ForeignKey(Horario)
    tipo_empleado = models.ForeignKey(TipoEmpleado)
    usuario = models.ForeignKey(Usuario)

    def __str__(self):
        return self.codigo

    class Meta:
        verbose_name_plural = 'Empleados'


class Nomina(models.Model):
    empleado = models.ForeignKey(Empleado)
    codigo = models.CharField(max_length=10, primary_key=True)
    sueldo = models.FloatField()
    rodamiento = models.FloatField()
    prestamo = models.FloatField()

    def _sueldofinal_(self):
        return self.sueldo - self.prestamo + self.rodamiento

    def __str__(self):
        return self.codigo

    class Meta:
        verbose_name_plural = 'Nomina'


class Permiso(models.Model):
    codigo = models.CharField(max_length=10, primary_key=True)
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField(max_length=140)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = 'Permisos'


class PermisoXUsuario(models.Model):
    usuario = models.ForeignKey(Usuario)
    permiso = models.ForeignKey(Permiso)


class TipoProducto(models.Model):
    codigo = models.CharField(max_length=10, primary_key=True)
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = 'Tipo de Productos'


class Producto(models.Model):
    tipo_producto = models.ForeignKey(TipoProducto)
    codigo = models.CharField(max_length=10, primary_key=True)
    nombre = models.CharField(max_length=50)
    fecha_vencimiento = models.DateField()
    precio_compra = models.FloatField()
    precio_venta = models.FloatField()
    cantidad = models.IntegerField()

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = 'Productos'


class Factura(models.Model):
    cliente = models.ForeignKey(Cliente)
    codigo = models.CharField(max_length=10, primary_key=True)
    fecha_venta = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.codigo)

    class Meta:
        verbose_name_plural = 'Facturas'


class ModoPago(models.Model):
    codigo = models.CharField(max_length=10, primary_key=True)
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField(max_length=140)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = 'Modos de pagos'


class DetalleFactura(models.Model):
    producto = models.ManyToManyField(Producto)
    codigo = models.ForeignKey(Factura)
    cantidad = models.IntegerField()
    valor = models.FloatField()

    def productos(self):
        return ",".join([str(p) for p in self.producto.all()])

    def __str__(self):
        return str(self.codigo)

    class Meta:
        ordering = ('producto',)

    class Meta:
        verbose_name_plural = 'Detalle de Facturas'
