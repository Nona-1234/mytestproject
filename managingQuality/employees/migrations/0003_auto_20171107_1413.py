# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-07 11:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0002_auto_20171024_1858'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='time_submit',
            field=models.DateTimeField(default=2017),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='employee',
            name='time_updated',
            field=models.DateTimeField(default=2017),
            preserve_default=False,
        ),
    ]
