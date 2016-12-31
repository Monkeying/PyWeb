# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-31 14:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PyWebApp', '0003_deviceform_history'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deviceform',
            name='SN',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='deviceform',
            name='alarm',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='deviceform',
            name='deviceName',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='deviceform',
            name='history',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='deviceform',
            name='lastUpdateTime',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='deviceform',
            name='temperature',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='userform',
            name='userEmail',
            field=models.EmailField(max_length=20),
        ),
    ]
