# -*- coding: UTF-8 -*-
from os import path
from django.core.urlresolvers import reverse
from django.test import TestCase
from catalogs.models import CatalogItem
from test_project import settings


__author__ = 'Razzhivin Alexander'
__email__ = 'admin@httpbots.com'



class HierarchyTest(TestCase):
    fixtures = ["catalogs_auth_user.json", "catalogs_catalogs.json", "catalogs_flatpages.json"]

    def setUp(self):
        self.auth = {
            "username": u"admin",
            "password": u"12345"
        }

    def test_get_root_catalog(self):
        catalog = CatalogItem.objects.get(pk=1)

        url = '{0}'.format(reverse('catalogs_list', args=['']))

        response = self.client.get(url)
        self.assertContains(response, catalog.name)

    def test_get_child_catalogs(self):
        catalog = CatalogItem.objects.get(pk=2)

        url = '{0}/'.format(reverse('catalogs_list', args=[catalog.path]))
        response = self.client.get(url)
        children = catalog.children.all()

        for child in children:
            self.assertContains(response, child.name)

    def test_duplicate_catalog_slug(self):
        catalog = CatalogItem.objects.get(pk=8)

        url = '{0}/'.format(reverse('catalogs_list', args=[catalog.path]))

        response = self.client.get(url)
        children = catalog.children.all()

        for child in children:
            self.assertContains(response, child.name)

    def test_url_redirects_without_slash(self):
        catalog = CatalogItem.objects.get(pk=2)

        url = '{0}'.format(reverse('catalogs_list', args=[catalog.path]))
        expected_url = '{0}/'.format(reverse('catalogs_list', args=[catalog.path]))

        response = self.client.get(url)
        self.assertRedirects(response, expected_url)

    def test_bind_catalog(self):
        self.client.login(**self.auth)

        data = {
            "description": u"index page",
            "parent": u"1",
            "url": u"/",
            "icon_url": u"",
            "next": u"http://127.0.0.1:8000/",
            "language_code": u"ru",
            "slug": u"index",
            "name": u"index",
            "icon": open(path.join(settings.STATICFILES_DIRS[0], "img/open_folder_gray.png"), "rb")
        }
        befor_catalog_items_count = CatalogItem.objects.count()
        url = reverse("catalogs_add_item", kwargs={"module_name": "flatpage", "pk": "1", "app_label": "flatpages"})
        response = self.client.post(url, data)
        self.assertRedirects(response, "http://127.0.0.1:8000/")
        self.assertEquals(befor_catalog_items_count+1, CatalogItem.objects.count())

        response = self.client.get("/")
        self.failUnlessEqual(response.status_code, 200)

        self.assertContains(response, data['name'])
        self.assertContains(response, data['slug'])
        self.assertContains(response, data['description'])

