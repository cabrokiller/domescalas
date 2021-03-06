# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-06-08 13:32
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('escalas', '0009_auto_20170607_1840'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ingreso',
            fields=[
                ('identificador', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='escalas.Identificador')),
                ('fing', models.DateField(blank=True, verbose_name=b'Fecha de Ingreso')),
                ('falta', models.DateField(blank=True, verbose_name=b'Fecha de Alta')),
                ('dispalta', models.CharField(blank=True, choices=[(0, b'Domicilio'), (1, b'CESMA'), (2, b'H de dia'), (3, b'Subagudos'), (4, b'Agudos'), (5, b'Otros')], max_length=2, verbose_name=b'Dispositivo de alta')),
            ],
        ),
        migrations.CreateModel(
            name='Zarit',
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
                ('item_16', models.PositiveSmallIntegerField(null=True)),
                ('item_17', models.PositiveSmallIntegerField(null=True)),
                ('item_18', models.PositiveSmallIntegerField(null=True)),
                ('item_19', models.PositiveSmallIntegerField(null=True)),
                ('item_20', models.PositiveSmallIntegerField(null=True)),
                ('item_21', models.PositiveSmallIntegerField(null=True)),
                ('item_22', models.PositiveSmallIntegerField(null=True)),
                ('identificador', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='escalas.Identificador')),
            ],
            options={
                'verbose_name': 'ZARIT',
                'verbose_name_plural': 'Escalas ZARIT',
            },
        ),
        migrations.AlterField(
            model_name='demo',
            name='laboral',
            field=models.CharField(blank=True, choices=[(b'1', b'Activo'), (b'2', b'Baja temporal'), (b'3', b'Sin trabajo actual'), (b'4', b'Pensionista'), (b'5', b'Nunca ha trabajado'), (b'6', b'Desconocido')], max_length=1, verbose_name=b'Situaci\xc3\xb3n laboral'),
        ),
        migrations.AlterField(
            model_name='demo',
            name='n_hijos',
            field=models.PositiveSmallIntegerField(blank=True, null=True, verbose_name=b'N\xc3\xbamero de hijos'),
        ),
        migrations.AlterField(
            model_name='demo',
            name='sector',
            field=models.CharField(blank=True, choices=[(b'1', b'AIS Gracia'), (b'2', b'AIS Dreta'), (b'3', b'AIS Guinard\xc3\xb3')], max_length=1, verbose_name=b'Sector'),
        ),
    ]
