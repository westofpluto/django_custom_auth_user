=============================
Django Custom User
=============================

.. image:: https://badge.fury.io/py/django_custom_user.svg
    :target: https://badge.fury.io/py/django_custom_user

.. image:: https://travis-ci.org/anthon-alindada/django_custom_user.svg?branch=master
    :target: https://travis-ci.org/anthon-alindada/django_custom_user

.. image:: https://codecov.io/gh/anthon-alindada/django_custom_user/branch/master/graph/badge.svg
    :target: https://codecov.io/gh/anthon-alindada/django_custom_user

Django custom user

Documentation
-------------

The full documentation is at https://django_custom_user.readthedocs.io.

Quickstart
----------

Install Django custom user::

    pip install django_custom_user

Add it to your `INSTALLED_APPS`:

.. code-block:: python

    INSTALLED_APPS = (
        ...
        'django_custom_user.apps.DjangoCustomUserConfig',
        ...
    )

Add Django Custom User's URL patterns:

.. code-block:: python

    from django_custom_user import urls as django_custom_user_urls


    urlpatterns = [
        ...
        url(r'^', include(django_custom_user_urls)),
        ...
    ]

Features
--------

* TODO

Running Tests
-------------

Does the code actually work?

::

    source <YOURVIRTUALENV>/bin/activate
    (myenv) $ pip install tox
    (myenv) $ tox

Credits
-------

Tools used in rendering this package:

*  Cookiecutter_
*  `cookiecutter-djangopackage`_

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`cookiecutter-djangopackage`: https://github.com/pydanny/cookiecutter-djangopackage
