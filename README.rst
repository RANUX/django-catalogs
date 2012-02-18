About
===============================================
django-catalogs - simple catalog structure for your site

Dependencies
===============================================
pip-requirements.txt

Installation
===============================================
Installation from github::

    pip install -e git+https://github.com/RANUX/django-catalogs#egg=django-catalogs


Examples
===============================================
test_project shows how to bind your application to catalog::

    cd django-catalogs/test_project
    python manage.py syncdb
    python manage.py runserver

Open http://127.0.0.1:8000/admin

    - add catalog item with slug "root"
    - add flat page catalog item to parent root catalog with slug "page"
    - add flat page with url /page/

Open http://127.0.0.1:8000/catalog/root/ and try to follow links. That's all:)


Future plans
===============================================
Localization