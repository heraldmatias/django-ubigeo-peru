from django import forms
from django.forms.widgets import Select, MultiWidget
from models import Ubigeo

class UbigeoWidget(MultiWidget):

    def __init__(self, regiones, provincias, distritos):
        self.regiones = regiones
	self.provincias = provincias
	self.distritos = distritos
	widgets = (
            Select(
                choices = self.regiones,
		attrs = {'onchange' : 'getProvincias(this.value, null, null);'}
            ),
            Select(
                choices = self.provincias,
		attrs = {'onchange' : 'getDistritos(this.value, null);'}
            ),
            Select(
                choices = self.distritos
            )
        )
        super(UbigeoWidget, self).__init__(widgets)

    def decompress(self, value):
        if value:
	    ubigeo = value if isinstance(value, Ubigeo) else Ubigeo.objects.get(
								ubigeo = value
								)
            self.widgets[1] = Select(
				choices=(
					(u[0], u[1]) for u in self.provincias
					), 
				attrs = {
				    'onchange' : 'getDistritos(this.value);'
					}
				)
            self.widgets[2] = Select(
				choices = (
					(u[0], u[1]) for u in self.distritos
					)
				)
            return (ubigeo.parent.parent.ubigeo,ubigeo.parent.ubigeo,ubigeo.ubigeo)
        return (None, None, None)

    class Media:
	js=(
	    'js/jquery.js',
	    'js/ubigeo.js',
	    )
