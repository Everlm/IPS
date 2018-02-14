# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AreaOftalmologia', '0003_auto_20151203_1922'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cliente',
            name='paciente',
        ),
        migrations.AlterField(
            model_name='cliente',
            name='persona',
            field=models.ForeignKey(to='AreaOftalmologia.Persona'),
        ),
    ]
