# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AreaOftalmologia', '0014_auto_20151208_1148'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='producto',
            name='codigo',
        ),
        migrations.AddField(
            model_name='producto',
            name='id',
            field=models.AutoField(default=2, auto_created=True, serialize=False, verbose_name='ID', primary_key=True),
            preserve_default=False,
        ),
    ]
