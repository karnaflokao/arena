# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader
from .models import Guerreiro, Partida
from django.db.models import Q

class dbz_rank():
    def __init__(self,posicao=0,guerreiro=None,partidas=0,pontos=0):
        self.posicao = posicao
        self.guerreiro = guerreiro
        self.partidas = partidas
        self.pontos = pontos
    
    def somarPartida(self,partida=1, ponto=0):
        self.partidas += partida
        self.pontos += ponto


def orderbyRank(allGuerreiros=[]):
        if len(allGuerreiros) <= 1:
            sA=allGuerreiros
        else:
            for j in range(0,len(allGuerreiros)):
                for i in range(0,len(allGuerreiros)-1):
                    if allGuerreiros[i].pontos < allGuerreiros[i+1].pontos:
                        Aux = allGuerreiros[i+1]
                        allGuerreiros[i+1]=allGuerreiros[i]
                        allGuerreiros[i]=Aux
            for j in range(0,len(allGuerreiros)):
                allGuerreiros[j].posicao = j+1
            sA=allGuerreiros
        return sA

def ranking(request):
    guerreiros = Guerreiro.objects.all()
    latest_dbz_list = []
    allGuerreiros = []
    for g in guerreiros:
        partidas = Partida.objects.filter(Q(gz1=g.id) | Q(gz2=g.id))
        d = dbz_rank()
        d.guerreiro = g.nome
        for p in partidas:
            if (p.gz1 == g):
                d.somarPartida(ponto=p.v1)
            else:
                d.somarPartida(ponto=p.v2)
        d.posicao = 1
        allGuerreiros.append(d)
    
    allGuerreiros = orderbyRank(allGuerreiros)
    latest_dbz_list = allGuerreiros
    template = loader.get_template('dbz/ranking.html')
    context = {
        'latest_dbz_list': latest_dbz_list,
    }
    return HttpResponse(template.render(context, request))