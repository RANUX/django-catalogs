# -*- coding: UTF-8 -*-
from django.contrib import admin
from catalogs.models import CatalogItem


__author__ = 'Razzhivin Alexander'
__email__ = 'admin@httpbots.com'

class CatalogItemAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        obj.save()
        obj.object_id=obj.id
        obj.save()


admin.site.register(CatalogItem, CatalogItemAdmin)