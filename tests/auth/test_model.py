# -*- coding: utf-8
# Core
import pytest
from mixer.backend.django import mixer

# Models
from django_custom_user.models import AuthToken
from django_custom_user.models import User


@pytest.mark.django_db
class TestAuthTokenModel():

    def test_auth_token_model(self):
        user = mixer.blend(User, username='username')
        auth_token = mixer.blend(AuthToken, token='token', user=user)

        assert isinstance(auth_token, AuthToken), \
            'Should create new AuthToken instance'

        assert str(auth_token) == 'token - username', \
            'Should be "{token} - {username}" format'
