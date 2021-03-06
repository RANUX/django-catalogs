# -*- coding: UTF-8 -*-
from django.contrib.contenttypes.models import ContentType
from django.core.urlresolvers import reverse
from django.test import TestCase
from catalogs.conf.settings import  PATH_SEPARATOR
from catalogs.models import CatalogItem


__author__ = 'Razzhivin Alexander'
__email__ = 'admin@httpbots.com'


class HierarchyTest(TestCase):
    fixtures = ['catalogs_catalogs']

    def setUp(self):
        self.content_type = ContentType.objects.get(name='catalog')


    def test_unicode(self):
        item = CatalogItem.objects.get(pk=7)
        self.assertEquals(item.__unicode__(), item.path)



    def test_root_slug_returns_self_for_root(self):
        item = CatalogItem.objects.get(pk=7)
        self.assertEqual(item.slug, item.root_slug)

    def test_root_slug(self):
        item = CatalogItem.objects.get(pk=6)
        root = CatalogItem.objects.get(pk=1)
        self.assertEqual(root.slug, item.root_slug)

    def test_root_has_depth_1(self):
        item = CatalogItem.objects.get(pk=7)
        self.assertEqual(1, item.depth)

    def test_item_depth(self):
        item = CatalogItem.objects.get(pk=2)
        self.assertEqual(2, item.depth)

    def test_build_root_path(self):
        item = CatalogItem(content_type=self.content_type)
        self.assert_empty_path(item)
        item.save()
        self.assertEquals(item.slug, item.path)

    def test_build_child_path(self):
        item = CatalogItem.objects.get(pk=6)
        child_item = CatalogItem(content_type=self.content_type, parent=item)
        self.assert_empty_path(child_item)
        child_item.save()

        self.assertEquals(
            item.path+PATH_SEPARATOR+child_item.slug,
            child_item.path
        )

    def assert_empty_path(self, item):
        self.assertEquals('', item.path)

    def test_has_children(self):
        item = CatalogItem.objects.create(content_type=self.content_type, name="eight", slug="eight")
        self.assertFalse(item.has_children())

        child = CatalogItem.objects.create(content_type=self.content_type, parent=item)
        self.assertTrue(item.has_children())

