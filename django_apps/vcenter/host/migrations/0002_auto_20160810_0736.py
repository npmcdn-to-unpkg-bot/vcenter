# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-08-10 07:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('host', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hostdetails',
            name='vcenterdate',
        ),
        migrations.AddField(
            model_name='hostdetails',
            name='vcenter_date',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='hostdetails',
            name='createdate',
            field=models.DateField(null=True),
        ),
    ]
