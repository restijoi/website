# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-10-19 02:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0008_project_tags'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='problem',
            field=models.TextField(blank=True, null=True),
        ),
    ]