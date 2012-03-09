# -*- coding: UTF-8 -*-
from django import forms
from django.contrib.contenttypes.models import ContentType
from catalogs.models import CatalogItem


__author__ = 'Razzhivin Alexander'
__email__ = 'admin@httpbots.com'


class CatalogItemForm(forms.ModelForm):

    language_code = forms.CharField(widget=forms.HiddenInput())

    class Meta:
        model = CatalogItem
        fields = (
            'url',
            'name',
            'slug',
            'description',
            'language_code',
            'icon',
            'icon_url',
            'parent',
        )

    def save(self, request, obj, *args, **kwargs):
        self.instance.creator = request.user
        self.instance.content_type = ContentType.objects.get_for_model(obj)
        self.instance.object_id = obj.id
        super(CatalogItemForm, self).save(*args, **kwargs)