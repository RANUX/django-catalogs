# -*- coding: UTF-8 -*-
from django.core.urlresolvers import reverse
from django.test import TestCase
from catalogs.models import CatalogItem


__author__ = 'Razzhivin Alexander'
__email__ = 'admin@httpbots.com'



class HierarchyTest(TestCase):
    fixtures = ['catalogs']

    def test_get_root_catalog(self):
        catalog = CatalogItem.objects.get(pk=1)

        url = '{0}'.format(reverse('catalogs_list', args=['']))

        response = self.client.get(url)
        self.assertContains(response, catalog.name)

    def test_get_child_catalogs(self):
        catalog = CatalogItem.objects.get(pk=2)

        url = '{0}/'.format(reverse('catalogs_list', args=[catalog.slug]))

        response = self.client.get(url)
        children = catalog.children.all()

        for child in children:
            self.assertContains(response, child.name)

    def test_url_redirects_without_slash(self):
        catalog = CatalogItem.objects.get(pk=2)

        url = '{0}'.format(reverse('catalogs_list', args=[catalog.slug]))
        expected_url = '{0}/'.format(reverse('catalogs_list', args=[catalog.slug]))

        response = self.client.get(url)
        self.assertRedirects(response, expected_url)