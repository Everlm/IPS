# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AreaOftalmologia', '0005_auto_20151205_1041'),
    ]

    operations = [
        migrations.RenameField(
            model_name='detallefactura',
            old_name='varlor',
            new_name='valor',
        ),
        migrations.RenameField(
            model_name='tratamiento',
            old_name='fehca_solicitud',
            new_name='fecha_solicitud',
        ),
        migrations.AddField(
            model_name='tipo_tratamiento',
            name='nombre',
            field=models.CharField(default=2, max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='cita',
            name='fecha',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='empleado',
            name='usuario',
            field=models.ForeignKey(to='AreaOftalmologia.Usuario'),
        ),
        migrations.AlterField(
            model_name='persona',
            name='fecha_nacimiento',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='producto',
            name='fecha_vencimiento',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='producto',
            name='nombre',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='tipo_producto',
            name='nombre',
            field=models.CharField(max_length=50),
        ),
    ]
