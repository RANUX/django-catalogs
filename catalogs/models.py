# -*- coding: UTF-8 -*-
import os
import urllib
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic
from django.core.exceptions import ObjectDoesNotExist
from django.core.files.base import File
from django.db import models
from django.utils.translation import ugettext_lazy as _
from easy_thumbnails.fields import ThumbnailerImageField
from conf.settings import ICON_WIDTH, ICON_HEIGHT, ICON_CROP_TYPE, ICON_PATH
from conf.settings import PATH_SEPARATOR
from conf.settings import  LANGUAGES


__author__ = 'Razzhivin Alexander'
__email__ = 'admin@httpbots.com'


class CatalogItemManager(models.Manager):
    def get_object_catalog_item(self, obj):
        object_type = ContentType.objects.get_for_model(obj)
        try:
            catalog_item = self.get(content_type__pk=object_type.id, object_id=obj.id)
        except ObjectDoesNotExist:
            return None
        return catalog_item


class CatalogItem(models.Model):

    ICON_SETTINGS = {
        'size': (ICON_WIDTH, ICON_HEIGHT),
        'crop': ICON_CROP_TYPE
    }

    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField(blank=True, null=True)
    content_object = generic.GenericForeignKey()

    name = models.CharField(_('name'), max_length=255)
    slug = models.SlugField(_('slug'), unique=True, max_length=150)
    hidden = models.BooleanField(_('hidden'), default=False)
    url = models.CharField(_('redirect url'), max_length=255, blank=True)
    description = models.TextField(_('description'), blank=True)

    language_code = models.CharField(_('language'), max_length=8, choices=LANGUAGES, default=dict(LANGUAGES).keys()[0])

    parent = models.ForeignKey('self', null=True, blank=True, default=None, related_name='children', verbose_name=_('parent catalog'))
    last_child = models.ForeignKey('self', null=True, blank=True, verbose_name=_('last child'))
    path = models.TextField(_('path'), editable=False, db_index=True)

    icon = ThumbnailerImageField(
        _('upload icon'),
        blank=True,
        upload_to=ICON_PATH,
        resize_source=ICON_SETTINGS
    )
    icon_url = models.URLField(_('icon url'), blank=True)

    objects = CatalogItemManager()

    class Meta(object):
        ordering = ('path',)
        verbose_name = _('catalog')
        verbose_name_plural = _('catalogs')

    def __unicode__(self):
        return self.path

    @property
    def depth(self):
        return len(self.path.split(PATH_SEPARATOR))

    @property
    def root_slug(self):
        return self.path.split(PATH_SEPARATOR)[0]

    def save(self, *args, **kwargs):
        super(CatalogItem, self).save(*args, **kwargs)
        self.set_object_id()

        path = self.slug
        if self.parent:
            path = PATH_SEPARATOR.join((self.parent.path, path))

            self.parent.last_child = self
            CatalogItem.objects.filter(slug=self.parent_id).update(last_child=self)

        self.path = path
        CatalogItem.objects.filter(slug=self.slug).update(path=self.path)
        self.store_icon_by_url()

    def set_object_id(self):
        if not self.object_id:
            self.object_id = self.id

    def store_icon_by_url(self):
        """Store icon locally if we have a URL"""
        if self.icon_url and not self.icon:

            result = urllib.urlretrieve(self.icon_url)
            self.icon.save(
                os.path.basename(self.icon_url),
                File(open(result[0]))
            )
            self.save()

    def has_children(self):
        return self.last_child is not None

    def get_absolute_url(self):
        return self.url or self.slug