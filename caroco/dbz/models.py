# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
from confronto.models import Confronto
from django.db.models import Q


class Season(models.Model):
    def __str__(self):
        return "%d Season" % self.temporada
    temporada = models.IntegerField('season', default=1)

class Guerreiro(models.Model):
    def __str__(self):
        return self.nome

    nome = models.CharField("Nome", max_length=200)
    season = models.ForeignKey(Season, on_delete=models.CASCADE, related_name='season')

    def exist_lowSeason(self,guerreiro):
        season = guerreiro.season
        for s in Season.objects.filter(id__lt=season.id):
            if len(Guerreiro.objects.filter(season=s)) > 0:
                return True
        return False

class Partida(models.Model):
    def __str__(self):
        return "%s %d x %d %s" % (self.gz1, self.v1, self.v2,self.gz2)

    gz1 = models.ForeignKey(Guerreiro, on_delete=models.CASCADE, related_name='gz1')
    v1 = models.IntegerField(default=0)
    gz2 = models.ForeignKey(Guerreiro, on_delete=models.CASCADE, related_name='gz2')
    v2 = models.IntegerField(default=0)
    confronto = models.ForeignKey(Confronto, on_delete=models.CASCADE)
    pSeason = models.ForeignKey(Season, on_delete=models.CASCADE, related_name='pSeason', default=1)

    def faltaLutar(self,guerreiro):
        latest_dbz_faltaJ = []
        allGuerreiros = Guerreiro.objects.filter(season__gte=guerreiro.season)
        allPartidas = self.allPartidas(guerreiro)

        for g in allGuerreiros:
            if g == guerreiro:
                continue
            inserir=True
            for p in allPartidas:
                if p.pSeason != guerreiro.season:
                    continue
                if p.gz2 == g:
                    inserir = False
                    break
            if inserir:
                latest_dbz_faltaJ.append(g)
        return latest_dbz_faltaJ

    def allPartidas(self, guerreiro):
        allPartidas = []
        for p in Partida.objects.filter(Q(gz1=guerreiro.id) | Q(gz2=guerreiro.id)).order_by('-pSeason'):
            if p.gz1 == guerreiro:
                allPartidas.append(p)
                continue
            else:
                newp=Partida()
                newp.gz1=p.gz2
                newp.v1=p.v2
                newp.gz2=p.gz1
                newp.v2=p.v1
                newp.pSeason = p.pSeason
                allPartidas.append(newp)

        return allPartidas

    def updateGuerreiroSeason(self, guerreiro):
        season = guerreiro.season
        newTemp = season.temporada+1
        newSeason = Season.objects.filter(temporada=newTemp)
        if len(newSeason) == None:
            nS = Season()
            nS.temporada = newTemp
            Season.save(nS)
            newSeason.append(nS)
        guerreiro.season=newSeason[0]
        Guerreiro.save(guerreiro)

    def save(self, *args, **kwargs):
        if not Guerreiro().exist_lowSeason(self.gz1):
            if len(self.faltaLutar(self.gz1))-1 <= 0:
                self.updateGuerreiroSeason(self.gz1)
        if not Guerreiro().exist_lowSeason(self.gz2):
            if len(self.faltaLutar(self.gz2))-1 <= 0:
                self.updateGuerreiroSeason(self.gz2)
        super(Partida, self).save(*args, **kwargs)

class Titulo(models.Model):
    def __str__(self):
        return self.nome

    nome = models.CharField("Titulo", max_length=200)
    pontosInicio = models.IntegerField("Pontos Iniciais", default=0)
    pontosFinal = models.IntegerField("Pontos Finais", default=10)
    foto = models.CharField("foto", max_length=200)




