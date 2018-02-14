# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AreaOftalmologia', '0029_auto_20160416_2015'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Tipo_Producto',
            new_name='TipoProducto',
        ),
    ]
