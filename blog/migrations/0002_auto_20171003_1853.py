# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-10-04 01:53
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='published_date',
            new_name='date',
        ),
    ]