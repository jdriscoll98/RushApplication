# -*- coding: utf-8 -*-
# Generated by Django 1.11.21 on 2019-07-11 20:54
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0008_auto_20190711_1640'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brother', models.CharField(max_length=100)),
                ('comment', models.TextField(max_length=300)),
                ('rushee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.Rushee')),
            ],
        ),
    ]
