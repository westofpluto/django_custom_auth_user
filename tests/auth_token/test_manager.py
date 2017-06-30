# -*- coding: utf-8
# Core
import pytest
from django.utils import timezone
from mixer.backend.django import mixer

# Model
from django_custom_user.auth_token.model import AuthToken


@pytest.mark.django_db
class TestAuthTokenManager():

    @pytest.fixture
    def auth_token_mock_data(self):
        mixer.cycle(4).blend(
            AuthToken,
            expiration_date=timezone.now() + timezone.timedelta(days=1))

        mixer.cycle(2).blend(
            AuthToken,
            expiration_date=timezone.now() + timezone.timedelta(days=-1))

    def test_get_all(self):
        mixer.cycle(4).blend(AuthToken)
        auth_token = AuthToken.objects.get_all()

        assert auth_token.count() == 4, 'Should get all auth tokens, 4'

    def test_find_by_id(self):
        mixer.blend(AuthToken, id=1)

        try:
            auth_token_should_exist = AuthToken.objects.find_by_id(id=1)
        except AuthToken.DoesNotExist:
            auth_token_should_exist = None

        try:
            auth_token_should_not_exist = AuthToken.objects.find_by_id(id=3)
        except AuthToken.DoesNotExist:
            auth_token_should_not_exist = None

        assert auth_token_should_exist is not None, \
            'Should get auth token by id'
        assert auth_token_should_not_exist is None, \
            'Should not get auth token by id'

    def test_find_by_token(self):
        mixer.blend(AuthToken, token='test_token')

        try:
            auth_token_should_exist = AuthToken.objects.find_by_token(
                token='test_token')
        except AuthToken.DoesNotExist:
            auth_token_should_exist = None

        try:
            auth_token_should_not_exist = AuthToken.objects.find_by_token(
                token='token')
        except AuthToken.DoesNotExist:
            auth_token_should_not_exist = None

        assert auth_token_should_exist is not None, \
            'Should get auth token by token'
        assert auth_token_should_not_exist is None, \
            'Should not get auth token by token'

    @pytest.mark.usefixtures('auth_token_mock_data')
    def test_filter_by_active(self):
        active_auth_tokens = AuthToken.objects.filter_by_active()

        assert active_auth_tokens.count() == 2, \
            'Should get all active auth tokens'

        for active_auth_token in active_auth_tokens:
            assert active_auth_token.expiration_date < timezone.now(), \
                'Should get all active auth tokens'

    @pytest.mark.usefixtures('auth_token_mock_data')
    def test_filter_by_expired(self):
        expired_auth_tokens = AuthToken.objects.filter_by_expired()

        assert expired_auth_tokens.count() == 4, \
            'Should get all expired auth tokens'

        for expired_auth_token in expired_auth_tokens:
            assert expired_auth_token.expiration_date > timezone.now(), \
                'Should get all expired auth tokens'
