# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-05-06 22:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dbz', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='titulo',
            name='pontosFinal',
            field=models.IntegerField(default=10, verbose_name='Pontos Finais'),
        ),
        migrations.AddField(
            model_name='titulo',
            name='pontosInicio',
            field=models.IntegerField(default=0, verbose_name='Pontos Iniciais'),
        ),
    ]
