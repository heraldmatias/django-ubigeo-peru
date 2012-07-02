# -*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils.encoding import smart_unicode

class Ubigeo(models.Model):
    ubigeo = models.CharField(_(u'Ubigeo'), max_length=6, primary_key=True)
    name   = models.CharField(_(u'Nombre'), max_length=140)
    parent = models.ForeignKey('self', related_name='+', null=True, blank=True)

    class Meta:
        verbose_name = _(u'Ubigeo')
        verbose_name_plural = _(u'Ubigeos')

    def __unicode__(self):
        return u'%s' % smart_unicode(self.name)
