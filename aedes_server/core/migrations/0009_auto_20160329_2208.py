# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-30 01:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_report_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='photo',
            field=models.ImageField(blank=True, upload_to='/upload/%Y/%m/%d/', verbose_name='foto'),
        ),
    ]