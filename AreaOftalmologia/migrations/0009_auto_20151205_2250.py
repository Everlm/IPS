# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AreaOftalmologia', '0008_auto_20151205_2244'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tratamiento',
            name='fecha_finalizacion',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='tratamiento',
            name='fecha_inicio',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='tratamiento',
            name='fecha_solicitud',
            field=models.DateField(auto_now_add=True),
        ),
    ]
