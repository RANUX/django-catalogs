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
        parent_catalog_item = None

        if url:
            if not url.endswith('/'):
                return HttpResponseRedirect("%s/" % request.path)

            splited_url = filter(None, url.split("/"))
            slug = splited_url[-1]
            path = '/'.join(splited_url)
            parent_catalog_item = CatalogItem.objects.filter(path=path, slug=slug, hidden=False)[0]

        catalog_items = CatalogItem.objects.filter(parent=parent_catalog_item, hidden=False).order_by('id')
        return self.render_to_response({'catalog': parent_catalog_item , 'catalog_items': catalog_items})

