# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-12 13:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_post_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='/home/daska/Documents/My_projects/Django/static/media'),
        ),
    ]
