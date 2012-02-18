# -*- coding: UTF-8 -*-
from setuptools import setup, find_packages
import sys

fktree = __import__('catalogs')


README_FILE = 'README.rst'


__author__ = 'Razzhivin Alexander'
__email__ = 'admin@httpbots.com'


try:
    long_description = open(README_FILE).read()
except IOError, err:
    sys.stderr.write("[ERROR] Cannot find file specified as "
                     "``long_description`` (%s)\n" % README_FILE)
    sys.exit(1)

setup(name='django-fktree',
    version=fktree.__version__,
    description='Django tree based on foreign key',
    long_description=long_description,
    zip_safe=False,
    author='Razzhivin Alexander',
    author_email='admin@httpbots.com',
    url='https://github.com/RANUX/django-fktree',
    download_url='https://github.com/RANUX/django-fktree/downloads',
    packages = find_packages(),
    include_package_data=True,
    install_requires = [
        'django>=1.3',
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