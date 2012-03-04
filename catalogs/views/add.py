# -*- coding: UTF-8 -*-
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.db.models.loading import get_model
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render_to_response
from django.template.context import RequestContext
from django.views.decorators.http import require_POST
from django.utils.translation import ugettext
from catalogs.forms import CatalogItemForm
from catalogs.models import CatalogItem


__author__ = 'Razzhivin Alexander'
__email__ = 'admin@httpbots.com'

def get_add_catalog_item_url(obj):
    return reverse('catalogs_add_item', kwargs={
        'app_label': obj._meta.app_label,
        'module_name': obj._meta.module_name,
        'pk': obj.pk
    })

@require_POST
@login_required
def add_catalog_item(request, app_label, module_name, pk, template_name='catalogs/add.html', extra_context={}):
    next = request.POST.get('next', '/')

    model = get_model(app_label, module_name)

    if model is None:
        return HttpResponseRedirect(next)

    obj = get_object_or_404(model, pk=pk)
    catalog_item = CatalogItem.objects.get_object_catalog_item(obj)
    form = CatalogItemForm(request.POST, request.FILES, instance=catalog_item)

    if form.is_valid():
        form.save(request, obj)
        request.user.message_set.create(message=ugettext('Added to catalog.'))
    return HttpResponseRedirect(next)



