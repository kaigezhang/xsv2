# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-04-07 15:58
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_auto_20180407_2348'),
    ]

    operations = [
        migrations.RenameField(
            model_name='oss',
            old_name='mine_type',
            new_name='mime_type',
        ),
    ]
