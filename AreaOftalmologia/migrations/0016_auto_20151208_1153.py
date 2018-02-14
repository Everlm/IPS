# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AreaOftalmologia', '0015_auto_20151208_1150'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='producto',
            name='id',
        ),
        migrations.AddField(
            model_name='producto',
            name='codigo',
            field=models.CharField(serialize=False, max_length=10, primary_key=True, default=2),
            preserve_default=False,
        ),
        migrations.RemoveField(
            model_name='producto',
            name='tipo_producto',
        ),
        migrations.AddField(
            model_name='producto',
            name='tipo_producto',
            field=models.ForeignKey(to='AreaOftalmologia.Tipo_Producto', default=2),
            preserve_default=False,
        ),
    ]
