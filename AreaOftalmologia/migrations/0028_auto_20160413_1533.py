# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AreaOftalmologia', '0027_auto_20160413_1530'),
    ]

    operations = [
        migrations.AlterField(
            model_name='persona',
            name='telefono',
            field=models.IntegerField(null=True),
        ),
    ]
