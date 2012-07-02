# -*- coding: utf-8 -*-
from django.contrib import admin
from models import Ubigeo

class UbigeoAdmin(admin.ModelAdmin):
    list_display = ('ubigeo','name',)
    search_fields  = ['name',] 
    list_per_page = 25
    list_max_show_all = 30

admin.site.register(Ubigeo, UbigeoAdmin)
