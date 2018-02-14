# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AreaOftalmologia', '0020_auto_20160321_2302'),
    ]

    operations = [
        migrations.AlterField(
            model_name='persona',
            name='identificacion',
            field=models.IntegerField(max_length=12, serialize=False, primary_key=True, help_text='introduce cedula'),
        ),
    ]
