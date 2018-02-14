# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AreaOftalmologia', '0013_auto_20151208_1147'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='tipo_producto',
            field=models.ManyToManyField(to='AreaOftalmologia.Tipo_Producto'),
        ),
    ]
