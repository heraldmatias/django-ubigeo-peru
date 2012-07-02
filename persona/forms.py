from django import forms
from models import Persona 
from ubigeo.fields import UbigeoFormField

class PersonaForm(forms.ModelForm):

    ubigeo = UbigeoFormField()

    def __init__(self, *args, **kwargs):
	super(PersonaForm, self).__init__(*args, **kwargs)

    class Meta:
	model = Persona
