from django import forms
from django.forms import ModelChoiceField
from django.core.exceptions import ValidationError
from widgets import UbigeoWidget
from models import Ubigeo
from django.db import models

class UbigeoFormField(forms.MultiValueField):

    DISTRICT_DEFAULT='010101'

    def __init__(self, *args, **kwargs):
        regiones   = Ubigeo.objects.filter(parent__isnull=True).order_by('name')
        provincias = Ubigeo.objects.filter(parent=regiones[0]).order_by('name')
        distritos  = Ubigeo.objects.filter(parent=provincias[0]).order_by('name')
        self.fields = (
            ModelChoiceField(queryset=regiones),
            ModelChoiceField(queryset=provincias),
            ModelChoiceField(queryset=distritos),
        )
        self.widget = UbigeoWidget(
                regiones = self.fields[0]._get_choices(),
                provincias = self.fields[1]._get_choices(),
                distritos = self.fields[2]._get_choices()
            )
        super(UbigeoFormField, self).__init__(
                            self.fields,
                            self.widget,
                            *args, 
                            **kwargs
                            )

    def compress(self, data_list):
        if data_list:
            return data_list[2]
            return None

    def clean(self, value):
        distrito = Ubigeo.objects.get(pk=value[2])
        self.fields[1].queryset = Ubigeo.objects.filter(
                            parent=distrito.parent.parent
                            )
        self.fields[2].queryset = Ubigeo.objects.filter(parent=distrito.parent)
        return distrito

    def prepare_value(self, value):
        if value is None:
            value=DISTRICT_DEFAULT
        distrito = Ubigeo.objects.get(pk=value)
        self.fields[1].queryset = Ubigeo.objects.filter(
                            parent=distrito.parent.parent
                            )
        self.fields[2].queryset = Ubigeo.objects.filter(parent=distrito.parent)
        self.widget.provincias = self.fields[1]._get_choices()
        self.widget.distritos = self.fields[2]._get_choices()
        self.widget.decompress(distrito)
        return value


class UbigeoField(models.ForeignKey):

    def __init__(self, *args, **kwargs):
        super(UbigeoField, self).__init__(Ubigeo, *args, **kwargs)