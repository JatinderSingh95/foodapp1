# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-06-09 09:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0017_remove_blog_zipcode'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='zipcode',
            field=models.CharField(default='', max_length=100),
        ),
    ]
