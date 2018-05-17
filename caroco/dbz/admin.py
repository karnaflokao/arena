# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from .models import Guerreiro, Partida, Titulo, Season

admin.site.register(Guerreiro)
admin.site.register(Partida)
admin.site.register(Titulo)
admin.site.register(Season)