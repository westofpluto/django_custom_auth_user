# -*- coding: utf-8
# Core
import pytest
from mixer.backend.django import mixer

# Model
from custom_auth_user.models import AuthToken

# Exception
from custom_auth_user.auth_token.exceptions import AuthenticationFailed

# Auth token service
from custom_auth_user.auth_token.authenticate_token \
    import AuthenticateTokenService


@pytest.mark.django_db
class TestAuthenticateToken():

    def test_authenticate_token(self):
        authenticate_token_service = AuthenticateTokenService(
            auth_token='invalid_token')

        try:
            user = authenticate_token_service.run()
        except AuthenticationFailed:
            user = None

        assert user is None, 'Should not authenticate user by token'

        mixer.blend(AuthToken, token='test_token')

        authenticate_token_service = AuthenticateTokenService(
            auth_token='test_token')

        try:
            user = authenticate_token_service.run()
        except AuthenticationFailed:
            user = None

        assert user, 'Should authenticate user by token'
