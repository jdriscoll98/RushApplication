# -*- coding: utf-8 -*-
# Generated by Django 1.11.21 on 2019-07-11 17:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rushee',
            name='brothers_known',
        ),
        migrations.AddField(
            model_name='rushee',
            name='currently_talking_to',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
