# -*- coding: utf-8
# Core
import pytest

# Model
from django_custom_user.models import User

# Exception
from django_custom_user.auth_token.exceptions import AuthenticationFailed

# Auth token service
from django_custom_user.auth_token.authenticate_user \
    import AuthenticateUserService


@pytest.mark.django_db
class TestAuthenticateUser():

    def test_authenticate_user(self):
        User.objects.create_superuser(
            email='email@email.com',
            password='emailpassword')
        User.objects.create_superuser(
            email='email@cloud.com',
            password='userpassword',
            username='username')

        authenticate_user_service = AuthenticateUserService(
            email_or_username='',
            password='')

        try:
            token = authenticate_user_service.run()
        except AuthenticationFailed:
            token = None

        assert token is None, 'Should not authenticate user'

        authenticate_user_service = AuthenticateUserService(
            email_or_username='email@email.com',
            password='emailpassword')

        try:
            token = authenticate_user_service.run()
        except AuthenticationFailed:
            token = None

        assert token, 'Should authenticate user by email'

        authenticate_user_service = AuthenticateUserService(
            email_or_username='username',
            password='userpassword')

        try:
            token = authenticate_user_service.run()
        except AuthenticationFailed:
            token = None

        assert token, 'Should authenticate user by password'
