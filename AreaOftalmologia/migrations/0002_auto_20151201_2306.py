# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AreaOftalmologia', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='modopago',
            options={'verbose_name_plural': 'Modos de pagos'},
        ),
    ]
