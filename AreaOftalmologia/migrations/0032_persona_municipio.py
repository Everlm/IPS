# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-26 00:38
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('AreaOftalmologia', '0031_auto_20160524_1110'),
    ]

    operations = [
        migrations.AddField(
            model_name='persona',
            name='municipio',
            field=models.ForeignKey(blank=True, default=2, on_delete=django.db.models.deletion.CASCADE, to='AreaOftalmologia.Municipio'),
            preserve_default=False,
        ),
    ]
