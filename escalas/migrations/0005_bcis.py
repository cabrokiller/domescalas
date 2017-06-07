# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-06-03 17:22
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('escalas', '0004_auto_20170320_1938'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bcis',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField()),
                ('item_01', models.PositiveSmallIntegerField(null=True)),
                ('item_02', models.PositiveSmallIntegerField(null=True)),
                ('item_03', models.PositiveSmallIntegerField(null=True)),
                ('item_04', models.PositiveSmallIntegerField(null=True)),
                ('item_05', models.PositiveSmallIntegerField(null=True)),
                ('item_06', models.PositiveSmallIntegerField(null=True)),
                ('item_07', models.PositiveSmallIntegerField(null=True)),
                ('item_08', models.PositiveSmallIntegerField(null=True)),
                ('item_09', models.PositiveSmallIntegerField(null=True)),
                ('item_10', models.PositiveSmallIntegerField(null=True)),
                ('item_11', models.PositiveSmallIntegerField(null=True)),
                ('item_12', models.PositiveSmallIntegerField(null=True)),
                ('item_13', models.PositiveSmallIntegerField(null=True)),
                ('item_14', models.PositiveSmallIntegerField(null=True)),
                ('item_15', models.PositiveSmallIntegerField(null=True)),
                ('identificador', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='escalas.Identificador')),
            ],
            options={
                'verbose_name': 'BCIS',
                'verbose_name_plural': 'Escalas BCIS',
            },
        ),
    ]