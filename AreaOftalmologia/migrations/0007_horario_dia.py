# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AreaOftalmologia', '0006_auto_20151205_1611'),
    ]

    operations = [
        migrations.AddField(
            model_name='horario',
            name='dia',
            field=models.CharField(choices=[('Lunes', 'Lunes'), ('Martes', 'Martes'), ('Miercoles', 'Miercoles'), ('Jueves', 'Jueves'), ('Viernes', 'viernes'), ('Sabado', 'Sabado')], max_length=20, default=2),
            preserve_default=False,
        ),
    ]
