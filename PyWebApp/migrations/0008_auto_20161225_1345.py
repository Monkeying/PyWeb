# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-25 05:45
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('PyWebApp', '0007_auto_20161225_0147'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userform',
            name='devices',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='PyWebApp.DeviceList'),
        ),
    ]