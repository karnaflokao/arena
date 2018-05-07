# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.template import loader
from .models import Confronto
from datetime import tzinfo, timedelta, datetime

ZERO = timedelta(0)

class UTC(tzinfo):
  def utcoffset(self, dt):
    return ZERO
  def tzname(self, dt):
    return "UTC"
  def dst(self, dt):
    return ZERO


def index(request):
    allConfronto = Confronto.objects.all()
    latest_confronto_list = []
    utc = UTC()
    for c in allConfronto:
        if c.data_jogo > datetime.now(utc):
            latest_confronto_list.append(c)
    template = loader.get_template('confronto/index.html')
    context = {
        'latest_confronto_list': latest_confronto_list,
    }
    return HttpResponse(template.render(context, request))

def detail(request, confronto_id):
    return HttpResponse("Voce esta olhando para o confronto %s." % confronto_id)
