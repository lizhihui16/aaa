# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-12-20 08:36
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0007_auto_20181220_0700'),
    ]

    operations = [
        migrations.RenameField(
            model_name='publisher',
            old_name='countrt',
            new_name='country',
        ),
    ]