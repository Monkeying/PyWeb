# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-25 06:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PyWebApp', '0008_auto_20161225_1345'),
    ]

    operations = [
        migrations.CreateModel(
            name='DeviceForm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deviceName', models.CharField(max_length=20)),
                ('SN', models.CharField(max_length=20)),
                ('tempreture', models.CharField(max_length=20)),
                ('lastUpdateTime', models.CharField(max_length=20)),
                ('alarm', models.CharField(max_length=20)),
            ],
        ),
        migrations.RemoveField(
            model_name='userform',
            name='devices',
        ),
        migrations.DeleteModel(
            name='deviceList',
        ),
        migrations.AddField(
            model_name='deviceform',
            name='users',
            field=models.ManyToManyField(to='PyWebApp.UserForm'),
        ),
    ]