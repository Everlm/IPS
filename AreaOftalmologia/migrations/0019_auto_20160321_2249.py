# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AreaOftalmologia', '0018_auto_20160321_2223'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nomina',
            name='prestamo',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='nomina',
            name='rodamiento',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='nomina',
            name='sueldo',
            field=models.FloatField(),
        ),
    ]
