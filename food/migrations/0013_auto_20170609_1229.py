# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-06-09 06:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0012_auto_20170609_1226'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='openingstatus',
            field=models.CharField(choices=[('Open', 'Open'), ('Opening Soon', 'Opening Soon')], default=0, max_length=60, unique=True),
        ),
    ]
