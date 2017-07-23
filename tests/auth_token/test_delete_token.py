# -*- coding: utf-8
# Core
import pytest
from mixer.backend.django import mixer

# Model
from custom_auth_user.models import AuthToken

# Exception
from custom_auth_user.auth_token.exceptions import TokenNotFound

# Auth token service
from custom_auth_user.auth_token.delete_token \
    import DeleteTokenService


@pytest.mark.django_db
class TestDeleteToken():

    def test_delete_token(self):
        delete_token_service = DeleteTokenService(
            token='invalid_token')

        try:
            is_token_deleted = delete_token_service.run()
        except TokenNotFound:
            is_token_deleted = None

        assert is_token_deleted is None, 'Should raise token not found'

        mixer.blend(AuthToken, token='test_token')

        delete_token_service = DeleteTokenService(
            token='test_token')

        try:
            delete_token_service.run()
            is_token_deleted = True
        except TokenNotFound:
            is_token_deleted = None

        assert is_token_deleted is True, 'Should delete token'
