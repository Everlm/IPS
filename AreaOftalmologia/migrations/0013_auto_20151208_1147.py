# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AreaOftalmologia', '0012_auto_20151206_2303'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='producto',
            name='id',
        ),
        migrations.AddField(
            model_name='producto',
            name='codigo',
            field=models.CharField(serialize=False, max_length=10, default=2, primary_key=True),
            preserve_default=False,
        ),
        migrations.RemoveField(
            model_name='producto',
            name='tipo_producto',
        ),
        migrations.AddField(
            model_name='producto',
            name='tipo_producto',
            field=models.ManyToManyField(to='AreaOftalmologia.Tipo_Producto', blank=True, null=True),
        ),
    ]
