# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AreaOftalmologia', '0004_auto_20151203_1931'),
    ]

    operations = [
        migrations.RenameField(
            model_name='persona',
            old_name='seegundo_nombre',
            new_name='segundo_nombre',
        ),
        migrations.AlterField(
            model_name='tipo_examen',
            name='nombre',
            field=models.CharField(max_length=50),
        ),
    ]
