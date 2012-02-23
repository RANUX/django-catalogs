#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import os
import sys
from optparse import OptionParser

from django.conf import settings

if not settings.configured:
    PROJECT_DIR, MODULE_NAME = os.path.split(
        (os.path.realpath(__file__))
    )

    settings.configure(
        DATABASE_ENGINE='sqlite3',
        DATABASES={
            'default': {
                'ENGINE': 'django.db.backends.sqlite3',
                },
            },
        ROOT_URLCONF = 'catalogs.urls',
        NOSE_ARGS = ['--nocapture',
                     '--all-modules',
                     '--nologcapture',
                     '--verbosity=2',
                     '--with-coverage',
                     '--cover-package=catalogs',
#                     '--cover-html',
                     #             '--with-doctest',
                     'catalogs'
                     #             '--cover-erase',
                     #             '--cover-tests',
        ],
        MIDDLEWARE_CLASSES = (
            'django.middleware.common.CommonMiddleware',
        ),
        TEMPLATE_LOADERS = (
            'django.template.loaders.filesystem.Loader',
            'django.template.loaders.app_directories.Loader',
        ),
        TEMPLATE_DIRS = (
            os.path.join(PROJECT_DIR, 'catalogs', 'tests', 'templates'),
        ),
        INSTALLED_APPS=[
            'django.contrib.auth',
            'django.contrib.contenttypes',
            'catalogs',
        ],
        DEBUG=False,
    )


from django_nose import NoseTestSuiteRunner

def runtests(*test_args, **kwargs):
    if not test_args:
        test_args = ['catalogs']

    test_runner = NoseTestSuiteRunner(**kwargs)
    failures = test_runner.run_tests(test_args)
    sys.exit(failures)

if __name__ == '__main__':
    parser = OptionParser()
    parser.add_option('--verbosity', dest='verbosity', action='store', default=1, type=int)
    parser.add_options(NoseTestSuiteRunner.options)
    (options, args) = parser.parse_args()

    runtests(*args, **options.__dict__)