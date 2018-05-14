# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader
from .models import Guerreiro, Partida, Titulo
from django.db.models import Q


class dbz_rank():
    def __init__(self,posicao=0,guerreiro=None,id=None,partidas=0,pontos=0,titulo=None,foto=None,season=0):
        self.posicao = posicao
        self.guerreiro = guerreiro
        self.id = id
        self.partidas = partidas
        self.pontos = pontos
        self.titulo = titulo
        self.foto = foto
        self.season = season


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

def getTitulo(guerreiro=None):
    for t in Titulo.objects.all():
        if guerreiro.pontos >= t.pontosInicio and guerreiro.pontos <= t.pontosFinal:
            return [t.nome, t.foto]

def createRanking(g=None):
    partidas = Partida.objects.filter(Q(gz1=g.id) | Q(gz2=g.id))
    d = dbz_rank()
    d.guerreiro = g.nome
    d.season = g.season
    d.id = g.id
    for p in partidas:
        if (p.gz1 == g):
            d.somarPartida(ponto=p.v1)
        else:
            d.somarPartida(ponto=p.v2)
    d.posicao = 1
    [d.titulo, d.foto] = getTitulo(d)
    return d

def index(request):
    template = loader.get_template('dbz/index.html')
    context = {
    }
    return HttpResponse(template.render(context, request))

def ranking(request):
    guerreiros = Guerreiro.objects.all()
    latest_dbz_list = []
    allGuerreiros = []
    for g in guerreiros:
        d = createRanking(g)
        allGuerreiros.append(d)

    allGuerreiros = orderbyRank(allGuerreiros)
    latest_dbz_list = allGuerreiros
    template = loader.get_template('dbz/ranking.html')
    context = {
        'latest_dbz_list': latest_dbz_list,
    }
    return HttpResponse(template.render(context, request))


def perfil(request,guerreiroId):

    template = loader.get_template('dbz/perfil.html')
    latest_dbz_guerreiro = Guerreiro.objects.filter(id=guerreiroId)
    allPartidas = Partida.objects.filter(Q(gz1=latest_dbz_guerreiro[0].id) | Q(gz2=latest_dbz_guerreiro[0].id))
    latest_dbz_partidas = []

    for p in allPartidas:
        if p.gz1 == latest_dbz_guerreiro[0]:
            latest_dbz_partidas.append(p)
            continue
        else:
            newp=Partida()
            newp.gz1=p.gz2
            newp.v1=p.v2
            newp.gz2=p.gz1
            newp.v2=p.v1
            latest_dbz_partidas.append(newp)

    latest_dbz_faltaJ = []
    allGuerreiros = Guerreiro.objects.all()
    for g in allGuerreiros:
        if g == latest_dbz_guerreiro[0]:
            continue
        inserir=True
        for p in latest_dbz_partidas:
            if p.gz2 == g:
                inserir = False
                break
        if inserir:
            latest_dbz_faltaJ.append(g)

    rank = createRanking(latest_dbz_guerreiro[0])
    titulo = rank.titulo
    foto = rank.foto

    context = {
       'latest_dbz_guerreiro': latest_dbz_guerreiro,
       'latest_dbz_partidas': latest_dbz_partidas,
       'latest_dbz_faltaJ': latest_dbz_faltaJ,
       'titulo': titulo,
       'foto': foto
    }
    return HttpResponse(template.render(context, request))
