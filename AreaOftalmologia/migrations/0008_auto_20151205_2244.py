# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AreaOftalmologia', '0007_horario_dia'),
    ]

    operations = [
        migrations.AlterField(
            model_name='persona',
            name='sexo',
            field=models.CharField(choices=[('Masculino', 'Masculino'), ('Femenino', 'Femenino')], max_length=20),
        ),
    ]
