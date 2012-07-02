# -*- coding: utf-8 -*-
from django.contrib.auth.decorators import login_required
from models import Ubigeo
from django.core import serializers
from django.http import HttpResponse

@login_required(login_url='/profile/login/')
def provincia(request):
    provincias = Ubigeo.objects.filter(parent = Ubigeo.objects.get(ubigeo = request.GET['r'])).order_by('name')
    return HttpResponse(serializers.serialize("json", provincias, ensure_ascii=False),mimetype='application/json')

@login_required(login_url='/profile/login/')
def distrito(request):
    distritos = Ubigeo.objects.filter(parent = Ubigeo.objects.get(ubigeo = request.GET['d'])).order_by('name')
    return HttpResponse(serializers.serialize("json", distritos, ensure_ascii=False),mimetype='application/json')
