# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-29 21:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_auto_20160327_0309'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cluster',
            options={'ordering': ('label',), 'verbose_name': 'aglomerado', 'verbose_name_plural': 'aglomerados'},
        ),
        migrations.AddField(
            model_name='report',
            name='device_id',
            field=models.CharField(default='not defined yet', max_length=255, verbose_name='ID do aparelho'),
            preserve_default=False,
        ),
    ]
