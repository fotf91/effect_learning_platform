# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-10-02 13:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account_app', '0002_auto_20160625_1650'),
    ]

    operations = [
        migrations.AddField(
            model_name='typeguser',
            name='top_skill_1',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
