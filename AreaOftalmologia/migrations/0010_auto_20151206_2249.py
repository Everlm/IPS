# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AreaOftalmologia', '0009_auto_20151205_2250'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='detallefactura',
            name='producto',
        ),
        migrations.AddField(
            model_name='detallefactura',
            name='producto',
            field=models.ManyToManyField(to='AreaOftalmologia.Producto'),
        ),
        migrations.AlterField(
            model_name='tratamiento',
            name='fecha_solicitud',
            field=models.DateField(auto_now=True),
        ),
    ]
