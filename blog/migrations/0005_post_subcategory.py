# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-12 13:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_post_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='subcategory',
            field=models.CharField(choices=[('BRG', 'Burger'), ('TRA', 'Traditional'), ('ASI', 'Asian'), ('FAST', 'Fastfood'), ('STR', 'Streetfood'), ('CAK', 'Cakes'), ('RAN', 'Random - to favourite')], default='BRG', max_length=3),
        ),
    ]