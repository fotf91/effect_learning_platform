# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-10-03 14:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account_app', '0007_auto_20161002_1453'),
    ]

    operations = [
        migrations.CreateModel(
            name='Specialization',
            fields=[
                ('name', models.CharField(max_length=60, primary_key=True, serialize=False)),
            ],
        ),
    ]
