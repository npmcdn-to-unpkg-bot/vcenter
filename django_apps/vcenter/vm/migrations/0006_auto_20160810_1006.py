# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-08-10 10:06
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vm', '0005_auto_20160810_1005'),
    ]

    operations = [
        migrations.RenameField(
            model_name='vmdetails',
            old_name='numVvirtualdisks',
            new_name='numvirtualdisks',
        ),
    ]
