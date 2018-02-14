# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AreaOftalmologia', '0023_auto_20160406_1625'),
    ]

    operations = [
        migrations.AlterField(
            model_name='persona',
            name='identificacion',
            field=models.IntegerField(serialize=False, help_text='introduce cedula', primary_key=True),
        ),
    ]
