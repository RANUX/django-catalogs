# -*- coding: UTF-8 -*-
from django.conf.urls.defaults import patterns, url
from catalogs.views.list import CatalogListView


__author__ = 'Razzhivin Alexander'
__email__ = 'admin@httpbots.com'


urlpatterns = patterns('',
    url(r'^(?P<url>.*)$', CatalogListView.as_view(), name='catalogs_list'),
)