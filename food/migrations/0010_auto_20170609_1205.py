# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-06-09 06:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0009_auto_20170609_1203'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='pincode',
        ),
        migrations.AddField(
            model_name='blog',
            name='zipcode',
            field=models.CharField(default=0, max_length=100),
        ),
    ]
