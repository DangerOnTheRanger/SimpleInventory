# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-24 07:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orderboard', '0003_auto_20160924_0640'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='stage',
            field=models.CharField(choices=[('W', 'Wanted'), ('O', 'Ordered'), ('R', 'Recieved'), ('A', 'Archived')], default='W', max_length=1),
        ),
    ]
