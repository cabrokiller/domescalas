# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-07-11 18:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('escalas', '0046_auto_20170711_1819'),
    ]

    operations = [
        migrations.AlterField(
            model_name='who_das',
            name='d1_1',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
