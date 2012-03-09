# -*- coding: UTF-8 -*-
from django.conf import settings


__author__ = 'Razzhivin Alexander'
__email__ = 'admin@httpbots.com'


PATH_SEPARATOR = getattr(settings, 'CATALOGS_PATH_SEPARATOR', '/')
LANGUAGES = getattr(settings, 'LANGUAGES')

ICON_PATH = getattr(settings, 'CATALOGS_ICON_PATH', 'catalogs/icons/')
ICON_WIDTH = getattr(settings, 'CATALOGS_ICON_WIDTH', 160)
ICON_HEIGHT = getattr(settings, 'CATALOGS_ICON_HEIGHT', 80)
ICON_CROP_TYPE = getattr(settings, 'CATALOGS_ICON_CROP_TYPE', 'smart')