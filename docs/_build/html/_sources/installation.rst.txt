============
Installation
============

Get the distribution
--------------------

Install Django custom user. In the command line::

    pip install django_custom_auth_user

Configuration
-------------

Add `'custom_auth_user'` it to your `INSTALLED_APPS`::

    INSTALLED_APPS = (
        ...
        'custom_auth_user',
        ...
    )

Set your ``AUTH_USER_MODEL`` setting to use ``custom_auth_user.User``::

    AUTH_USER_MODEL = 'custom_auth_user.User'

Create the database tables. In the command line::

    python manage.py migrate
