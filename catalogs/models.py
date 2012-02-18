# -*- coding: UTF-8 -*-
from django.db import models
from django.utils.translation import ugettext_lazy as _
from easy_thumbnails.fields import ThumbnailerImageField
from model_utils.managers import InheritanceManager
from conf.settings import ICON_WIDTH, ICON_HEIGHT, ICON_CROP_TYPE, ICON_PATH
from conf.settings import PATH_SEPARATOR
from conf.settings import  LANGUAGES


__author__ = 'Razzhivin Alexander'
__email__ = 'admin@httpbots.com'


class CatalogItem(models.Model):

    ICON_SETTINGS = {
        'size': (ICON_WIDTH, ICON_HEIGHT),
        'crop': ICON_CROP_TYPE
    }

    name = models.CharField(_('name'), max_length=255)
    slug = models.SlugField(unique=True)
    deleted = models.BooleanField(_('deleted'), default=False)

    language_code = models.CharField(_('language'), max_length=8, choices=LANGUAGES, default=dict(LANGUAGES).keys()[0])

    parent = models.ForeignKey('self', null=True, blank=True, default=None, related_name='children', verbose_name=_('parent'))
    last_child = models.ForeignKey('self', null=True, blank=True, verbose_name=_('last child'))
    path = models.TextField(_('path'), editable=False, db_index=True)

    icon = ThumbnailerImageField(
        _('icon'),
        blank=True,
        upload_to=ICON_PATH,
        resize_source=ICON_SETTINGS
    )

    objects = InheritanceManager()

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

        path = self.slug
        if self.parent:
            path = PATH_SEPARATOR.join((self.parent.path, path))

            self.parent.last_child = self
            CatalogItem.objects.filter(slug=self.parent_id).update(last_child=self)

        self.path = path
        CatalogItem.objects.filter(slug=self.slug).update(path=self.path)

    def has_children(self):
        return self.last_child is not None

    def get_absolute_url(self):
        return None