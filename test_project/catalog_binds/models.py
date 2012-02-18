# -*- coding: UTF-8 -*-
from django.db import models
from catalogs.models import CatalogItem

__author__ = 'Razzhivin Alexander'
__email__ = 'admin@httpbots.com'

class FlatPageCatalogItem(CatalogItem):

    def get_absolute_url(self):
        return '/%s/' % self.slug