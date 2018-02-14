# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AreaOftalmologia', '0010_auto_20151206_2249'),
    ]

    operations = [
        migrations.AlterField(
            model_name='detallefactura',
            name='producto',
            field=models.ManyToManyField(null=True, blank=True, to='AreaOftalmologia.Producto'),
        ),
    ]
