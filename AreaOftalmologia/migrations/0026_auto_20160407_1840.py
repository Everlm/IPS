# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AreaOftalmologia', '0025_auto_20160406_1758'),
    ]

    operations = [
        migrations.AlterField(
            model_name='persona',
            name='identificacion',
            field=models.CharField(help_text='introduce cedula', max_length=12, primary_key=True, serialize=False),
        ),
    ]
