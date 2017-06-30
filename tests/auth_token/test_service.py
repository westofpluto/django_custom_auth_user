# -*- coding: utf-8
# Core
import pytest
from mixer.backend.django import mixer

# Models
from django_custom_user.user.model import User
from django_custom_user.auth_token.model import AuthToken

# Service
from django_custom_user.auth_token.service import AuthTokenService


@pytest.mark.django_db
class TestAuthTokenService():

    def test_create(self):
        user = mixer.blend(User)
        auth_token = AuthTokenService().create(user=user)

        assert isinstance(auth_token, AuthToken), \
            'Should create new AuthToken instance'

    def test_generate_token(self):
        mixer.blend(AuthToken, token='test_token')

        token = AuthTokenService().generate_token(token='test_token')

        assert token is not 'test_token', \
            'Should generate new token'
