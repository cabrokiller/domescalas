# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-06-10 13:20
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('escalas', '0015_auto_20170609_1755'),
    ]

    operations = [
        migrations.AlterField(
            model_name='identificador',
            name='codigo',
            field=models.CharField(help_text='Siglas nombre + fecha ingreso: p.e. "ABC24122016', max_length=100, validators=[django.core.validators.RegexValidator(message='Formato incorrecto (XYZddmmaaaa)', regex='\\b[A-Z]{3}\\d{8}')]),
        ),
    ]
