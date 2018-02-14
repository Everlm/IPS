# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AreaOftalmologia', '0028_auto_20160413_1533'),
    ]

    operations = [
        migrations.CreateModel(
            name='TipoTratamiento',
            fields=[
                ('codigo', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
                ('descripcion', models.TextField(max_length=140)),
            ],
            options={
                'verbose_name_plural': 'Tipos de tratamientos',
            },
        ),
        migrations.RenameModel(
            old_name='Especialidad_Medica',
            new_name='EspecialidadMedica',
        ),
        migrations.RenameModel(
            old_name='Historia_Clinica',
            new_name='HistoriaClinica',
        ),
        migrations.RenameModel(
            old_name='Tipo_Empleado',
            new_name='TipoEmpleado',
        ),
        migrations.RenameModel(
            old_name='Tipo_Examen',
            new_name='TipoExamen',
        ),
        migrations.AlterField(
            model_name='persona',
            name='telefono',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='tratamiento',
            name='tipo_tratamiento',
            field=models.ForeignKey(to='AreaOftalmologia.TipoTratamiento'),
        ),
        migrations.DeleteModel(
            name='Tipo_Tratamiento',
        ),
    ]
