# -*- coding: utf-8 -*-
# Generated by Django 1.11.21 on 2019-07-11 19:22
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0005_auto_20190711_1522'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rushee',
            name='email',
        ),
    ]
