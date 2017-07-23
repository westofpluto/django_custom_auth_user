# -*- coding: utf-8
# Core
import pytest
from mixer.backend.django import mixer

# Models
from custom_auth_user.models import User
from custom_auth_user.models import AuthToken

# Store
from custom_auth_user.auth_token.store import AuthTokenStore

# Commands
from custom_auth_user.auth_token.commands.authenticate_token_command \
    import authenticate_token


@pytest.mark.django_db
class TestAuthenticateTokenCommand():

    @pytest.fixture
    def auth_token_store(self):
        return AuthTokenStore()

    def test_authenticate_token_command(self, auth_token_store):
        mixer.blend(AuthToken, token='test_token')

        user = authenticate_token(
            auth_token_store=auth_token_store,
            auth_token='invalid')

        assert user is None, 'Should not be authenticated by token'

        user = authenticate_token(
            auth_token_store=auth_token_store,
            auth_token='test_token')

        assert user, 'Should be authenticated by token'

    def test_authenticate_disabled_user(self, auth_token_store):
        user = mixer.blend(User, is_disabled=True)
        mixer.blend(AuthToken, token='test_token', user=user)

        user = authenticate_token(
            auth_token_store=auth_token_store,
            auth_token='test_token')

        assert user is None, 'Should not authenticate disabled user'

    def test_authenticate_inactive_user(self, auth_token_store):
        user = mixer.blend(User, is_active=False)
        mixer.blend(AuthToken, token='test_token', user=user)

        user = authenticate_token(
            auth_token_store=auth_token_store,
            auth_token='test_token')

        assert user is None, 'Should not authenticate inactive user'
