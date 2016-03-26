# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-26 06:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('latitude', models.FloatField(verbose_name='latitude')),
                ('longitude', models.FloatField(verbose_name='longitude')),
                ('category', models.CharField(choices=[('F', 'Foco'), ('C', 'Criadouro'), ('S', 'Suspeita')], max_length=1, verbose_name='category')),
                ('reported_at', models.DateTimeField(auto_now_add=True, verbose_name='reportado em')),
            ],
        ),
    ]
