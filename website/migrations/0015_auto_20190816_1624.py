# -*- coding: utf-8 -*-
# Generated by Django 1.11.21 on 2019-08-16 20:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0014_merge_20190816_1623'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rushee',
            name='grade',
            field=models.CharField(choices=[('', 'GRADE'), ('FRESHMAN', 'FRESHMAN'), ('SOPHOMORE', 'SOPHOMORE'), ('JUNIOR', 'JUNIOR'), ('SENIOR', 'SENIOR')], max_length=100),
        ),
    ]