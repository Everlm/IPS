# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cargo',
            fields=[
                ('codigo', models.CharField(primary_key=True, serialize=False, max_length=10)),
                ('nombre', models.CharField(max_length=20)),
                ('descripcion', models.TextField(max_length=100)),
            ],
            options={
                'verbose_name_plural': 'Cargos',
            },
        ),
        migrations.CreateModel(
            name='Cita',
            fields=[
                ('codigo', models.CharField(primary_key=True, serialize=False, max_length=10)),
                ('fecha', models.DateTimeField()),
                ('hora', models.TimeField()),
            ],
            options={
                'verbose_name_plural': 'Citas',
            },
        ),
        migrations.CreateModel(
            name='Ciudad',
            fields=[
                ('codigo', models.CharField(primary_key=True, serialize=False, max_length=10)),
                ('nombre', models.CharField(max_length=30)),
            ],
            options={
                'verbose_name_plural': 'Ciudades',
            },
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('codigo', models.CharField(primary_key=True, serialize=False, max_length=10)),
            ],
            options={
                'verbose_name_plural': 'Clientes',
            },
        ),
        migrations.CreateModel(
            name='Departamento',
            fields=[
                ('codigo', models.CharField(primary_key=True, serialize=False, max_length=10)),
                ('nombre', models.CharField(max_length=30)),
            ],
            options={
                'verbose_name_plural': 'Departamentos',
            },
        ),
        migrations.CreateModel(
            name='DetalleFactura',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.CharField(max_length=4)),
                ('varlor', models.CharField(max_length=30)),
            ],
            options={
                'verbose_name_plural': 'Detalle de Facturas',
            },
        ),
        migrations.CreateModel(
            name='Empleado',
            fields=[
                ('codigo', models.CharField(primary_key=True, serialize=False, max_length=10)),
                ('cargo', models.ForeignKey(to='AreaOftalmologia.Cargo')),
            ],
            options={
                'verbose_name_plural': 'Empleados',
            },
        ),
        migrations.CreateModel(
            name='Eps',
            fields=[
                ('codigo', models.CharField(primary_key=True, serialize=False, max_length=10)),
                ('nombre', models.CharField(max_length=30)),
            ],
            options={
                'verbose_name_plural': 'EPS',
            },
        ),
        migrations.CreateModel(
            name='Especialidad_Medica',
            fields=[
                ('codigo', models.CharField(primary_key=True, serialize=False, max_length=10)),
                ('nombre', models.CharField(max_length=30)),
            ],
            options={
                'verbose_name_plural': 'Especialidad medica',
            },
        ),
        migrations.CreateModel(
            name='Examen',
            fields=[
                ('codigo', models.CharField(primary_key=True, serialize=False, max_length=10)),
                ('nombre', models.CharField(max_length=30)),
                ('fecha_solicitud', models.DateTimeField()),
                ('fecha_aplicacion', models.DateTimeField(auto_now_add=True)),
                ('observaciones', models.TextField(max_length=100)),
            ],
            options={
                'verbose_name_plural': 'Examenes',
            },
        ),
        migrations.CreateModel(
            name='Factura',
            fields=[
                ('codigo', models.CharField(primary_key=True, serialize=False, max_length=10)),
                ('fecha_venta', models.DateTimeField(auto_now_add=True)),
                ('cliente', models.ForeignKey(to='AreaOftalmologia.Cliente')),
            ],
            options={
                'verbose_name_plural': 'Facturas',
            },
        ),
        migrations.CreateModel(
            name='Historia_Clinica',
            fields=[
                ('codigo', models.CharField(primary_key=True, serialize=False, max_length=10)),
            ],
            options={
                'verbose_name_plural': 'Historias Clinicas',
            },
        ),
        migrations.CreateModel(
            name='Horario',
            fields=[
                ('codigo', models.CharField(primary_key=True, serialize=False, max_length=10)),
                ('hora_inicio', models.TimeField()),
                ('hora_fin', models.TimeField()),
            ],
            options={
                'verbose_name_plural': 'Horarios',
            },
        ),
        migrations.CreateModel(
            name='Incapacidad',
            fields=[
                ('codigo', models.CharField(primary_key=True, serialize=False, max_length=10)),
                ('fecha', models.DateTimeField()),
                ('dias', models.CharField(max_length=10)),
            ],
            options={
                'verbose_name_plural': 'Incapacidades',
            },
        ),
        migrations.CreateModel(
            name='Medico',
            fields=[
                ('codigo', models.CharField(primary_key=True, serialize=False, max_length=10)),
                ('eps', models.ForeignKey(to='AreaOftalmologia.Eps')),
                ('especialidad', models.ForeignKey(to='AreaOftalmologia.Especialidad_Medica')),
            ],
            options={
                'verbose_name_plural': 'Medicos',
            },
        ),
        migrations.CreateModel(
            name='ModoPago',
            fields=[
                ('codigo', models.CharField(primary_key=True, serialize=False, max_length=10)),
                ('nombre', models.CharField(max_length=10)),
                ('descripcion', models.TextField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Municipio',
            fields=[
                ('codigo', models.CharField(primary_key=True, serialize=False, max_length=10)),
                ('nombre', models.CharField(max_length=30)),
                ('departamento', models.ForeignKey(to='AreaOftalmologia.Departamento')),
            ],
            options={
                'verbose_name_plural': 'Municipios',
            },
        ),
        migrations.CreateModel(
            name='Nomina',
            fields=[
                ('codigo', models.CharField(primary_key=True, serialize=False, max_length=10)),
                ('sueldo', models.CharField(blank=True, max_length=20)),
                ('rodamiento', models.CharField(blank=True, max_length=20)),
                ('prestamo', models.CharField(blank=True, max_length=20)),
                ('empleado', models.ForeignKey(to='AreaOftalmologia.Empleado')),
            ],
            options={
                'verbose_name_plural': 'Nomina',
            },
        ),
        migrations.CreateModel(
            name='Paciente',
            fields=[
                ('codigo', models.CharField(primary_key=True, serialize=False, max_length=12)),
                ('eps', models.ForeignKey(to='AreaOftalmologia.Eps')),
                ('historia_clinica', models.ForeignKey(to='AreaOftalmologia.Historia_Clinica')),
            ],
            options={
                'verbose_name_plural': 'Pacientes',
            },
        ),
        migrations.CreateModel(
            name='Permiso',
            fields=[
                ('codigo', models.CharField(primary_key=True, serialize=False, max_length=10)),
                ('nombre', models.CharField(max_length=10)),
                ('descripcion', models.TextField(max_length=100)),
            ],
            options={
                'verbose_name_plural': 'Permisos',
            },
        ),
        migrations.CreateModel(
            name='PermisoXUsuario',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('permiso', models.ForeignKey(to='AreaOftalmologia.Permiso')),
            ],
        ),
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('identificacion', models.CharField(primary_key=True, serialize=False, max_length=12)),
                ('primer_nombre', models.CharField(max_length=30)),
                ('seegundo_nombre', models.CharField(max_length=30)),
                ('primer_apellido', models.CharField(max_length=30)),
                ('segundo_apellido', models.CharField(max_length=30)),
                ('telefono', models.CharField(max_length=10)),
                ('direccion', models.CharField(max_length=20)),
                ('tipo_de_sangre', models.CharField(max_length=4)),
                ('sexo', models.CharField(max_length=2)),
                ('fecha_nacimiento', models.DateTimeField(auto_now_add=True)),
                ('correo_electronico', models.EmailField(max_length=30)),
                ('ciudad', models.ForeignKey(to='AreaOftalmologia.Ciudad', blank=True)),
            ],
            options={
                'verbose_name_plural': 'Personas',
            },
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('codigo', models.CharField(primary_key=True, serialize=False, max_length=10)),
                ('nombre', models.CharField(max_length=10)),
                ('fecha_vencimiento', models.DateTimeField()),
                ('precio_compra', models.CharField(max_length=20)),
                ('precio_venta', models.CharField(max_length=20)),
                ('cantidad', models.CharField(max_length=4)),
            ],
            options={
                'verbose_name_plural': 'Productos',
            },
        ),
        migrations.CreateModel(
            name='Resultados',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=10)),
                ('fecha_entrega', models.DateTimeField(auto_now_add=True)),
                ('descripcion', models.TextField(max_length=100)),
                ('historia_clinica', models.ForeignKey(to='AreaOftalmologia.Historia_Clinica')),
            ],
            options={
                'verbose_name_plural': 'Resultados de examenes',
            },
        ),
        migrations.CreateModel(
            name='Tipo_Empleado',
            fields=[
                ('codigo', models.CharField(primary_key=True, serialize=False, max_length=10)),
                ('nombre', models.CharField(max_length=20)),
                ('descripcion', models.TextField(max_length=100)),
            ],
            options={
                'verbose_name_plural': 'Tipos de empleados',
            },
        ),
        migrations.CreateModel(
            name='Tipo_Examen',
            fields=[
                ('codigo', models.CharField(primary_key=True, serialize=False, max_length=10)),
                ('nombre', models.CharField(max_length=20)),
            ],
            options={
                'verbose_name_plural': 'Tipos de examenes',
            },
        ),
        migrations.CreateModel(
            name='Tipo_Producto',
            fields=[
                ('codigo', models.CharField(primary_key=True, serialize=False, max_length=10)),
                ('nombre', models.CharField(max_length=10)),
            ],
            options={
                'verbose_name_plural': 'Tipo de Productos',
            },
        ),
        migrations.CreateModel(
            name='Tipo_Tratamiento',
            fields=[
                ('codigo', models.CharField(primary_key=True, serialize=False, max_length=10)),
                ('descripcion', models.TextField(max_length=30)),
            ],
            options={
                'verbose_name_plural': 'Tipos de tratamientos',
            },
        ),
        migrations.CreateModel(
            name='Tratamiento',
            fields=[
                ('codigo', models.CharField(primary_key=True, serialize=False, max_length=10)),
                ('nombre', models.CharField(max_length=30)),
                ('fehca_solicitud', models.DateTimeField()),
                ('fecha_inicio', models.DateTimeField(auto_now_add=True)),
                ('fecha_finalizacion', models.DateTimeField()),
                ('observaciones', models.TextField(max_length=100)),
                ('precio', models.CharField(max_length=20)),
                ('historia_clinica', models.ForeignKey(to='AreaOftalmologia.Historia_Clinica')),
                ('incapacidad', models.ForeignKey(to='AreaOftalmologia.Incapacidad')),
                ('medico', models.ForeignKey(to='AreaOftalmologia.Medico')),
                ('tipo_tratamiento', models.ForeignKey(to='AreaOftalmologia.Tipo_Tratamiento')),
            ],
            options={
                'verbose_name_plural': 'Tratamientos',
            },
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('codigo', models.CharField(primary_key=True, serialize=False, max_length=10)),
                ('nombre', models.CharField(unique=True, max_length=10)),
            ],
            options={
                'verbose_name_plural': 'Usuarios',
            },
        ),
        migrations.AddField(
            model_name='resultados',
            name='tipo_examen',
            field=models.ForeignKey(to='AreaOftalmologia.Tipo_Examen'),
        ),
        migrations.AddField(
            model_name='producto',
            name='tipo_producto',
            field=models.ForeignKey(to='AreaOftalmologia.Tipo_Producto'),
        ),
        migrations.AddField(
            model_name='permisoxusuario',
            name='usuario',
            field=models.ForeignKey(to='AreaOftalmologia.Usuario'),
        ),
        migrations.AddField(
            model_name='paciente',
            name='persona',
            field=models.ForeignKey(to='AreaOftalmologia.Persona'),
        ),
        migrations.AddField(
            model_name='medico',
            name='persona',
            field=models.ForeignKey(to='AreaOftalmologia.Persona'),
        ),
        migrations.AddField(
            model_name='examen',
            name='historia_clinica',
            field=models.ForeignKey(to='AreaOftalmologia.Historia_Clinica'),
        ),
        migrations.AddField(
            model_name='examen',
            name='tipo_examen',
            field=models.ForeignKey(to='AreaOftalmologia.Tipo_Examen'),
        ),
        migrations.AddField(
            model_name='empleado',
            name='horario',
            field=models.ForeignKey(to='AreaOftalmologia.Horario'),
        ),
        migrations.AddField(
            model_name='empleado',
            name='persona',
            field=models.ForeignKey(to='AreaOftalmologia.Persona'),
        ),
        migrations.AddField(
            model_name='empleado',
            name='tipo_empleado',
            field=models.ForeignKey(to='AreaOftalmologia.Tipo_Empleado'),
        ),
        migrations.AddField(
            model_name='empleado',
            name='usuario',
            field=models.ForeignKey(to='AreaOftalmologia.Usuario', blank=True),
        ),
        migrations.AddField(
            model_name='detallefactura',
            name='codigo',
            field=models.ForeignKey(to='AreaOftalmologia.Factura'),
        ),
        migrations.AddField(
            model_name='detallefactura',
            name='producto',
            field=models.ForeignKey(to='AreaOftalmologia.Producto'),
        ),
        migrations.AddField(
            model_name='cliente',
            name='paciente',
            field=models.ForeignKey(to='AreaOftalmologia.Paciente', blank=True),
        ),
        migrations.AddField(
            model_name='cliente',
            name='persona',
            field=models.ForeignKey(to='AreaOftalmologia.Persona', blank=True),
        ),
        migrations.AddField(
            model_name='ciudad',
            name='departamento',
            field=models.ForeignKey(to='AreaOftalmologia.Departamento'),
        ),
        migrations.AddField(
            model_name='cita',
            name='especialidad',
            field=models.ForeignKey(to='AreaOftalmologia.Especialidad_Medica'),
        ),
        migrations.AddField(
            model_name='cita',
            name='medico',
            field=models.ForeignKey(to='AreaOftalmologia.Medico'),
        ),
        migrations.AddField(
            model_name='cita',
            name='paciente',
            field=models.ForeignKey(to='AreaOftalmologia.Paciente'),
        ),
    ]
