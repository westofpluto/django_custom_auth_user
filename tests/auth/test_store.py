# -*- coding: utf-8
# Core
import pytest
from mixer.backend.django import mixer

# Models
from django_custom_user.models import User
from django_custom_user.models import AuthToken

# Store
from django_custom_user.auth.store import AuthTokenStore


@pytest.mark.django_db
class TestAuthTokenStore():

    @pytest.fixture
    def auth_token_store(self):
        return AuthTokenStore()

    def test_save(self, auth_token_store):
        user = mixer.blend(User, email='email@email.com')
        auth_token = AuthToken(token='token', user=user)
        auth_token_store.save(auth_token=auth_token)

        try:
            auth_token = AuthToken.objects.find_by_token('token')
        except AuthToken.DoesNotExist:
            auth_token = None

        assert auth_token, 'Should save auth token data in database'
