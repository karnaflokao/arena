# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-05-17 15:00
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dbz', '0005_auto_20180517_1144'),
    ]

    operations = [
        migrations.AddField(
            model_name='partida',
            name='pSeason',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='pSeason', to='dbz.Season'),
        ),
    ]
