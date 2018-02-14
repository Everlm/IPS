# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AreaOftalmologia', '0002_auto_20151201_2306'),
    ]

    operations = [
        migrations.AlterField(
            model_name='persona',
            name='correo_electronico',
            field=models.EmailField(max_length=30, blank=True),
        ),
        migrations.AlterField(
            model_name='persona',
            name='direccion',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='persona',
            name='identificacion',
            field=models.CharField(max_length=12, serialize=False, primary_key=True, help_text='introduce cedula'),
        ),
    ]
