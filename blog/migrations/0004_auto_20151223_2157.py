# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-23 15:57
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_subcategory'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='categories',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='Postcategory', to='blog.Subcategory'),
        ),
    ]
