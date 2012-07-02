====================
Django-Ubigeo-Peru
====================

django-ubigeo-peru, es una app que te permitira implementar facilmente 
los ubigeos de Perú, en tus django app.

Instalar
-------

En tu settings.py
> INSTALLED_APPS = ( 
>
>     ......    
>
>     'ubigeo',
>
>)
>

En tu urls.py
> urlpatterns = patterns('',
>  
>     .....
>     (r'^ubigeo/', include('ubigeo.urls')),
>
>) 
