====================
Django-Ubigeo-Peru
====================

django-ubigeo-peru, es una app que te permitira implementar facilmente 
los ubigeos de Perú, en tus django app.

Instalar
-------

En tu settings.py

>
> INSTALLED_APPS = ( 
>
>     ......    
>     'ubigeo',
>
>)
>


En tu urls.py

> 
> urlpatterns = patterns('',
>  
>     .....
>     (r'^ubigeo/', include('ubigeo.urls')),
>
>)  
>

Usar
----
En tu models.py:

>
>from ubigeo.models import Ubigeo
> class MyModel(models.Model):
>     name = models.CharField(max_length=120)
>     ubigeo = models.ForeignKey(Ubigeo)
>

en tu forms.py:

>
> from ubigeo.models import Ubigeo
> from ubigeo.fields import UbigeoFormField
> class MyModelForm(form.ModelForm):
>     ubigeo = UbigeoFormFiel()
>     class Meta:
>         model = Ubigeo
