# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-23 02:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0002_auto_20170422_2222'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='date',
            field=models.DateTimeField(),
        ),
    ]
