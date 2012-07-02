from django.db import models
from ubigeo.models import Ubigeo
from ubigeo.fields import UbigeoField

class Persona(models.Model):
    name = models.CharField(max_length=150)
    ubigeo = models.ForeignKey(Ubigeo)
