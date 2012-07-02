from django import forms
from models import Ubigeo
from fields import UbigeoField

class UbigeoForm(forms.ModelForm):
    class Meta:
        model = Ubigeo

class UbigeoSelect(forms.Form):

    ubigeo = UbigeoFormField()
    
    def __init__(self, *args, **kwargs):
        super(UbigeoSelect, self).__init__(*args, **kwargs)
        if self.data:
            regiones   = Ubigeo.objects.filter(parent__isnull=True).order_by('name')
            provincias = Ubigeo.objects.filter(parent=self.data['ubigeo_0']).order_by('name')
            distritos  = Ubigeo.objects.filter(parent=self.data['ubigeo_1']).order_by('name')
            self.fields['ubigeo'].fields[0].queryset = regiones
            self.fields['ubigeo'].fields[1].queryset = provincias
            self.fields['ubigeo'].fields[2].queryset = distritos
