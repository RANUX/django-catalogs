# -*- coding: UTF-8 -*-
from setuptools import setup, find_packages
import sys

catalogs = __import__('catalogs')


README_FILE = 'README.rst'


__author__ = 'Razzhivin Alexander'
__email__ = 'admin@httpbots.com'


try:
    long_description = open(README_FILE).read()
except IOError, err:
    sys.stderr.write("[ERROR] Cannot find file specified as "
                     "``long_description`` (%s)\n" % README_FILE)
    sys.exit(1)

setup(name='django-catalogs',
    version=catalogs.__version__,
    description='Django based simple catalog structure for site',
    long_description=long_description,
    zip_safe=False,
    author='Razzhivin Alexander',
    author_email='admin@httpbots.com',
    url='https://github.com/RANUX/django-catalogs',
    download_url='https://github.com/RANUX/django-catalogs/downloads',
    packages = find_packages(exclude=['test_project',]),
    include_package_data=True,
    install_requires = [
        'django==1.3',
        'easy-thumbnails',
        'django-model-utils ',

        ### Required to build documentation
        # 'sphinx',
    ],
    test_suite='runtests.runtests',
    tests_require=['nose', 'django-nose', 'coverage'],
    classifiers = ['Development Status :: 1 - Beta',
                   'Environment :: Web Environment',
                   'Framework :: Django',
                   'Intended Audience :: Developers',
                   'License :: OSI Approved :: BSD License',
                   'Operating System :: OS Independent',
                   'Programming Language :: Python',
                   'Topic :: Utilities'],
)