# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
from confronto.models import Confronto

class Season(models.Model):
    def __str__(self):
        return "Season - %d" % self.season
    temporada = models.IntegerField('season', default=1)

class Guerreiro(models.Model):
    def __str__(self):
        return self.nome

    nome = models.CharField("Nome", max_length=200)
    season = models.ForeignKey(Season, on_delete=models.CASCADE, related_name='season')

class Partida(models.Model):
    def __str__(self):
        return "%s %d x %d %s" % (self.gz1, self.v1, self.v2,self.gz2)

    gz1 = models.ForeignKey(Guerreiro, on_delete=models.CASCADE, related_name='gz1')
    v1 = models.IntegerField(default=0)
    gz2 = models.ForeignKey(Guerreiro, on_delete=models.CASCADE, related_name='gz2')
    v2 = models.IntegerField(default=0)
    confronto = models.ForeignKey(Confronto, on_delete=models.CASCADE)

class Titulo(models.Model):
    def __str__(self):
        return self.nome

    nome = models.CharField("Titulo", max_length=200)
    pontosInicio = models.IntegerField("Pontos Iniciais", default=0)
    pontosFinal = models.IntegerField("Pontos Finais", default=10)
    foto = models.CharField("foto", max_length=200)




