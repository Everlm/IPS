# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AreaOftalmologia', '0011_auto_20151206_2258'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='producto',
            name='codigo',
        ),
        migrations.AddField(
            model_name='producto',
            name='id',
            field=models.AutoField(serialize=False, verbose_name='ID', default=2, auto_created=True, primary_key=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='detallefactura',
            name='producto',
            field=models.ManyToManyField(to='AreaOftalmologia.Producto'),
        ),
    ]
