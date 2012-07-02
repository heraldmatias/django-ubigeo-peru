# -*- coding: utf-8 -*-                                                          
from django.contrib import admin                                                 
from models import Persona
from forms import PersonaForm

class PersonaAdmin(admin.ModelAdmin):
    form=PersonaForm

admin.site.register(Persona, PersonaAdmin)
