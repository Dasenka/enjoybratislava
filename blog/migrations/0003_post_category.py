# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-12 12:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20170312_1134'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='category',
            field=models.CharField(choices=[('FOO', 'Eat'), ('BAR', 'Drink'), ('PLA', 'Where to go')], default='FOO', max_length=3),
        ),
    ]
