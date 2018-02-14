# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AreaOftalmologia', '0017_auto_20160313_1709'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nomina',
            name='prestamo',
            field=models.DecimalField(max_digits=10, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='nomina',
            name='rodamiento',
            field=models.DecimalField(max_digits=10, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='nomina',
            name='sueldo',
            field=models.DecimalField(max_digits=10, decimal_places=2),
        ),
    ]
