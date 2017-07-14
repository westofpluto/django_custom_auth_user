# -*- coding: utf-8
# Core
import pytest
from mixer.backend.django import mixer

# Models
from django_custom_user.models import User
from django_custom_user.models import AuthToken

# Store
from django_custom_user.auth_token.store import AuthTokenStore


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

        assert auth_token, 'Should save auth token data'

    def test_create(self, auth_token_store):
        user = mixer.blend(User)
        auth_token = auth_token_store.create(user=user)

        assert isinstance(auth_token, AuthToken), 'Should create auth token'

    def test_token_generator(self, auth_token_store):
        mixer.blend(AuthToken, token='test_token')
        token = auth_token_store.generate_token(token='test_token')

        assert len(token) is 32, \
            'Should create 32 lengthened token without duplicate'
