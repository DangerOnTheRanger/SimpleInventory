# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-09 22:27
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('SimpleInventory', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Board',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('desc', models.TextField()),
                ('active', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Stage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('index', models.IntegerField()),
                ('active', models.BooleanField(default=False)),
            ],
        ),
        migrations.AddField(
            model_name='item',
            name='archived',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='item',
            name='stage',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='SimpleInventory.Stage'),
        ),
        migrations.AddField(
            model_name='item',
            name='board',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='SimpleInventory.Board'),
        ),
    ]
