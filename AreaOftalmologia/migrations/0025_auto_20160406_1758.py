# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AreaOftalmologia', '0024_auto_20160406_1636'),
    ]

    operations = [
        migrations.AlterField(
            model_name='persona',
            name='telefono',
            field=models.IntegerField(),
        ),
    ]
