# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-10-02 14:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account_app', '0004_remove_typeguser_top_skill_1'),
    ]

    operations = [
        migrations.AddField(
            model_name='typeguser',
            name='top_skill_1',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
