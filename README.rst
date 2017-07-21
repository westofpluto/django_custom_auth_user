=======================
Django Custom Auth User
=======================

.. image:: https://travis-ci.org/anthon-alindada/django_custom_auth_user.svg?branch=master
    :target: https://travis-ci.org/anthon-alindada/django_custom_auth_user

.. image:: https://codecov.io/gh/anthon-alindada/django_custom_auth_user/branch/master/graph/badge.svg
  :target: https://codecov.io/gh/anthon-alindada/django_custom_auth_user

Documentation
-------------

The full documentation is at https://django_custom_auth_user.readthedocs.io.

Quickstart
----------

Install Django custom user::

    pip install django_custom_auth_user

Add it to your `INSTALLED_APPS`:

.. code-block:: python

    INSTALLED_APPS = (
        ...
        'custom_auth_user',
        ...
    )

Set your ``AUTH_USER_MODEL`` setting to use ``custom_auth_user.User``:

.. code-block:: python

    AUTH_USER_MODEL = 'custom_auth_user.User'

Create the database tables:

.. code-block:: python

    python manage.py migrate

Usage
-----

Custom user
-----------

Use ``get_user_model()`` to get user. For example:

.. code-block:: python

    from django.contrib.auth import get_user_model

    user = get_user_model().objects.get(email="user@cloud.com")

Use ``AUTH_USER_MODEL`` for model relations. For example:

.. code-block:: python

    from django.conf import settings
    from django.db import models

    class Post(models.Model):
        author = models.ForeignKey(settings.AUTH_USER_MODEL)

Or you can use ``custom_auth_user.models.AbstractUser`` to extend custom user. For example:

.. code-block:: python

    from custom_auth_user.models import AbstractUser

    class CustomUser(AbstractUser):
        """
        User model extends AbstractUser
        """
        pass

Then change the ``AUTH_USER_MODEL`` in settings to use new custom user.

.. code-block:: python

    AUTH_USER_MODEL = 'app.CustomUser'

User registration service
-------------------------

Use ``RegistrationService`` to register new user.

.. code-block:: python

    from custom_auth_user.user.registration import RegistrationService
    from custom_auth_user.user.exceptions import InvalidInput

    # Initialize registration service
    registration_service = RegistrationService(
        email=request.POST.get('email', ''),
        username=request.POST.get('username', ''),
        first_name=request.POST.get('first_name', ''),
        last_name=request.POST.get('last_name', ''),
        password=request.POST.get('password', ''))

    # Catch errors here
    try:
        user = registration_service.run()
    except InvalidInput:
        errors = registration_service.get_registration_form_errors()

Generate auth token
-------------------

Use ``AuthenticateUserService`` to generate new auth token.

.. code-block:: python

    from custom_auth_user.auth_token.authenticate_user import AuthenticateUserService
    from custom_auth_user.auth_token.exceptions import AuthenticationFailed

    authentication_service = AuthenticateUserService(
        email_or_username=request.POST.get('email_or_username', ''),
        password=request.POST.get('password', ''))

    try:
        token = authentication_service.run()
    except AuthenticationFailed:
        # Authentication failed
        pass

Token authentication
--------------------

Use ``token_required`` decorator to authenticate header token. Get authenticated user at ``request.user``.

Authorization header must have token at the begining. Example ``token 5KxXkJYwWBsN9Zne87ncoQYYuggDBdYY``.

Return json response if authentication failed.

.. code-block:: python

    from custom_auth_user.auth_token.decorators import token_required

    @token_required
    def my_view(request):
        # get authenticated user at request.user
        pass

Or you can use ``AuthenticateTokenService`` to authenticate token.

.. code-block:: python

    from custom_auth_user.auth_token.authenticate_token import AuthenticateTokenService
    from custom_auth_user.auth_token.exceptions import AuthenticationFailed

    authentication_service = AuthenticateTokenService(
        auth_token=request.POST.get('token', ''))

    try:
        user = authentication_service.run()
    except AuthenticationFailed:
        # Authentication failed
        pass

Delete Token
------------

Use ``DeleteTokenService`` to delete token. You can use this when user logs out.

.. code-block:: python

    from custom_auth_user.auth_token.delete_token import DeleteTokenService
    from custom_auth_user.auth_token.exceptions import TokenNotFound

    delete_token_service = DeleteTokenService(
        token=request.POST.get('token', ''))

    try:
        delete_token_service.run()
    except TokenNotFound:
        # Token not found
        pass

Extra features
--------------

User QuerySets
--------------

.. code-block:: python

    # Get all users
    users = User.objects.get_all()

    # Get find user by id
    user = User.objects.find_by_id(id=1)

    # Get find usermame by id
    user = User.objects.find_by_username(username='user')

    # Get find email by id
    user = User.objects.find_by_email(email='user@cloud.com')

    # Filter active users
    users = User.objects.filter_by_active()

    # Filter inactive users
    users = User.objects.filter_by_inactive()

    # Filter enabled users
    users = User.objects.filter_by_enabled()

    # Filter disabled users
    users = User.objects.filter_by_disabled()

AuthToken QuerySets
--------------

.. code-block:: python

    # Get all auth token
    token = AuthToken.objects.get_all()

    # Find by id
    token = AuthToken.objects.find_by_id(id=1)

    # Find by token
    token = AuthToken.objects.find_by_token(token='token')

    # Filter by active or unexpired tokens
    token = AuthToken.objects.filter_by_active()

    # Filter by expired token
    token = AuthToken.objects.filter_by_expired()
