# -*- coding: utf-8
# Core
import pytest
from mixer.backend.django import mixer

# Models
from custom_auth_user.auth_token.model import AuthToken

# Stores
from custom_auth_user.auth_token.store import AuthTokenStore

# Commands
from custom_auth_user.auth_token.commands.delete_token_command \
    import delete_token


@pytest.mark.django_db
class TestDeleteTokenCommand():

    @pytest.fixture
    def auth_token_store(self):
        return AuthTokenStore()

    def test_create_auth_token_command(self, auth_token_store):
        token = mixer.blend(AuthToken, token='test_token')

        is_token_deleted = delete_token(
            auth_token_store=auth_token_store,
            token='test_token')

        assert is_token_deleted is True, 'Should delete auth token'

        # Double check if token is deleted
        try:
            token = auth_token_store.query_set.find_by_token('test_token')
        except AuthToken.DoesNotExist:
            token = None

        assert token is None, 'Should delete auth token'
