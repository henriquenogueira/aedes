# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-26 22:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_cluster'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cluster',
            name='label',
            field=models.IntegerField(unique=True, verbose_name='etiqueta'),
        ),
    ]