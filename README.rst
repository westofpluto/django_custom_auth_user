Django Custom Auth User - Improved Fork
=======================================

This is a fork of https://github.com/anthon-alindada/django_custom_auth_user which fixes several bugs.
Unfortunately the original repo (the one I forked from) is no longer maintained by the developer,
even though it has a couple of critical bugs that render that repo unusable. In particular:

* In the original repo, the token expires 24 hours after the Django system gets restarted. Any tokens created after that will already be expired!
* In the original repo, the token_required decorator did not work on class-based view methods

Both of these issues have been fixed in this fork.

Here is the original README:

Django Custom Auth User
=======================
.. image:: https://travis-ci.org/anthon-alindada/django_custom_auth_user.svg?branch=master
    :target: https://travis-ci.org/anthon-alindada/django_custom_auth_user

.. image:: https://codecov.io/gh/anthon-alindada/django_custom_auth_user/branch/master/graph/badge.svg
    :target: https://codecov.io/gh/anthon-alindada/django_custom_auth_user

Django custom user model and abstract user model basic token authentication.

Documentation
-------------

The full documentation is at https://django_custom_auth_user.readthedocs.io.

Features
--------
* Custom user
* Extendable abstract user
* User registration service
* Token authentication
* Create auth token
* Delete auth token
* Query sets for ``User`` & ``AuthToken``

Quickstart
----------

Install Django custom user::

    pip install django_custom_auth_user


Add it to your ``INSTALLED_APPS``::

    INSTALLED_APPS = (
        ...
        'custom_auth_user',
        ...
    )

Set your ``AUTH_USER_MODEL`` setting to use ``custom_auth_user.User``::

    AUTH_USER_MODEL = 'custom_auth_user.User'

Create the database tables::

    python manage.py migrate


Version 0.1 (2017-07-23)
~~~~~~~~~~~~~~~~~~~~~~~~

- Initial release.
