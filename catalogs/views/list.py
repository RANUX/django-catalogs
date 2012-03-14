# -*- coding: UTF-8 -*-
from django.utils.translation import ugettext_lazy as _
from django.http import  HttpResponseRedirect
from django.views.generic.base import TemplateView
from catalogs.models import CatalogItem


__author__ = 'Razzhivin Alexander'
__email__ = 'admin@httpbots.com'


class CatalogListView(TemplateView):
    template_name = 'catalogs/list.html'

    def get(self, request, *args, **kwargs):
        url = kwargs.get('url')
        catalog_item = None

        if url:
            if not url.endswith('/'):
                return HttpResponseRedirect("%s/" % request.path)

            slug = filter(None, url.split("/"))[-1]  # filter removes empty strings
            catalog_item = CatalogItem.objects.get(slug=slug, hidden=False)

        catalog_items = CatalogItem.objects.filter(parent=catalog_item, hidden=False)
        return self.render_to_response({'catalog': catalog_item , 'catalog_items': catalog_items})

