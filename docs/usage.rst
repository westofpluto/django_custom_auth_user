=====
Usage
=====

Custom user
-----------

Use ``get_user_model()`` to get user. For example::

    from django.contrib.auth import get_user_model

    user = get_user_model().objects.get(email="user@cloud.com")

Use ``AUTH_USER_MODEL`` for model relations. For example::

    from django.conf import settings
    from django.db import models

    class Post(models.Model):
        author = models.ForeignKey(settings.AUTH_USER_MODEL)

Or you can use ``custom_auth_user.models.AbstractUser`` to extend custom user. For example::

    from custom_auth_user.models import AbstractUser

    class CustomUser(AbstractUser):
        """
        User model extends AbstractUser
        """
        pass

Then change the ``AUTH_USER_MODEL`` in settings to use new custom user::

    AUTH_USER_MODEL = 'app.CustomUser'

User registration
-----------------

Use ``RegistrationService`` to register new user::

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

Auth token generate
-------------------

Use ``AuthenticateUserService`` to generate new auth token::

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

Return json response if authentication failed::

    from custom_auth_user.auth_token.decorators import token_required

    @token_required
    def my_view(request):
        # get authenticated user at request.user
        pass

Or you can use ``AuthenticateTokenService`` to authenticate token::

    from custom_auth_user.auth_token.authenticate_token import AuthenticateTokenService
    from custom_auth_user.auth_token.exceptions import AuthenticationFailed

    authentication_service = AuthenticateTokenService(
        auth_token=request.POST.get('token', ''))

    try:
        user = authentication_service.run()
    except AuthenticationFailed:
        # Authentication failed
        pass

Auth token deletion
-------------------

Use ``DeleteTokenService`` to delete token. You can use this when user logs out::

    from custom_auth_user.auth_token.delete_token import DeleteTokenService
    from custom_auth_user.auth_token.exceptions import TokenNotFound

    delete_token_service = DeleteTokenService(
        token=request.POST.get('token', ''))

    try:
        delete_token_service.run()
    except TokenNotFound:
        # Token not found
        pass
