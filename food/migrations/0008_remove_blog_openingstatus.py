# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-06-09 06:20
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0007_blog_my_field'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='openingstatus',
        ),
    ]
