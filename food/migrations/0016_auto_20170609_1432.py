# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-06-09 09:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0015_auto_20170609_1335'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='facebookpage',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='blog',
            name='otherdetails',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='blog',
            name='twitterhandle',
            field=models.CharField(default='', max_length=100),
        ),
    ]
