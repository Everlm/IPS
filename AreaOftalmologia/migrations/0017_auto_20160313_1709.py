# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AreaOftalmologia', '0016_auto_20151208_1153'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tipo_examen',
            name='nombre',
            field=models.CharField(max_length=100),
        ),
    ]
