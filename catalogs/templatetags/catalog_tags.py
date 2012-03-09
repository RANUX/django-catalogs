# -*- coding: UTF-8 -*-
from django.contrib.contenttypes.models import ContentType
from django.core.urlresolvers import reverse
from django.template import Library
from catalogs.forms import CatalogItemForm
from catalogs.models import CatalogItem
from catalogs.views.add import get_add_catalog_item_url

register = Library()


__author__ = 'Razzhivin Alexander'
__email__ = 'admin@httpbots.com'

@register.inclusion_tag('catalogs/add_form.html', takes_context=True)
def add_to_catalog_form(context, obj):
    """
    Renders a "add to catalog" form.

    The user must own ``catalogs.add_to_catalog permission`` to add
    videos.
    """
    if context['user'].has_perm('catalogs.add_to_catalog'):
        catalog_item = CatalogItem.objects.get_object_catalog_item(obj)
        data = None

        if not catalog_item:
            data={
                'language_code': context['request'].LANGUAGE_CODE,
            }

        form = CatalogItemForm(
            data=data,
            instance=catalog_item,
        )

        return {
            'form': form,
            'form_url': get_add_catalog_item_url(obj),
            'next': context['request'].build_absolute_uri(),
            }
    else:
        return {'form': None}