# -*- coding: UTF-8 -*-
from django.conf.urls.defaults import patterns, url
from catalogs.views.add import add_catalog_item
from catalogs.views.list import CatalogListView


__author__ = 'Razzhivin Alexander'
__email__ = 'admin@httpbots.com'


urlpatterns = patterns('',
    url(r'^add-catalog-item/(?P<app_label>[\w\-]+)/(?P<module_name>[\w\-]+)/(?P<pk>\d+)/$', add_catalog_item, name='catalogs_add_item'),
    url(r'^(?P<url>.*)$', CatalogListView.as_view(), name='catalogs_list'),
)