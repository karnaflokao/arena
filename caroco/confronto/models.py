# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
# Create your models here.

from datetime import timedelta

class Jogo(models.Model):
    def __str__(self):
        return self.nome

    nome = models.CharField(max_length=200)

class Confronto(models.Model):
    def __str__(self):
        data_jogo = self.data_jogo - timedelta(hours = 3)
        return "%s: %s x %s - %s" % (self.jogo, self.time1, self.time2, data_jogo)

    time1 = models.CharField(max_length=200)
    time2 = models.CharField(max_length=200)
    data_jogo  = models.DateTimeField('Data Confronto')
    data_reserv  = models.DateTimeField('Data Reserva', auto_now=True)
    jogo = models.ForeignKey(Jogo, on_delete=models.CASCADE)
    valendo = models.BooleanField(default=True)
