About
===============================================
django-catalogs - simple catalog structure for your site.
You can add any object to catalog structure.

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

    - create catalog item with name and slug "root"
    - create flat page. For example with "/" url

Open http://127.0.0.1:8000/ and add index page to catalog
Open http://127.0.0.1:8000/catalogs/, folow links. That's all :)


Future plans
===============================================
  - Localization