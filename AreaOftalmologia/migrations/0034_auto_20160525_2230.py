# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-26 03:30
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('AreaOftalmologia', '0033_auto_20160525_2216'),
    ]

    operations = [
        migrations.AlterField(
            model_name='persona',
            name='municipio',
            field=models.ForeignKey(blank=True, default='no tiene', null=True, on_delete=django.db.models.deletion.CASCADE, to='AreaOftalmologia.Municipio'),
        ),
    ]