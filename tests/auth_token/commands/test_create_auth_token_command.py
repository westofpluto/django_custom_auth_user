# Core
import pytest
from mixer.backend.django import mixer

# Models
from django_custom_user.models import User
from django_custom_user.models import AuthToken

# Store
from django_custom_user.auth_token.store import AuthTokenStore

# Commands
from django_custom_user.auth_token.commands.create_auth_token_command \
    import create_auth_token


@pytest.mark.django_db
class TestCreateAuthTokenCommand():

    @pytest.fixture
    def auth_token_store(self):
        return AuthTokenStore()

    def test_create_auth_token_command(self, auth_token_store):
        user = mixer.blend(User)
        auth_token = create_auth_token(
            auth_token_store=auth_token_store,
            user=user)

        assert isinstance(auth_token, AuthToken), 'Should create auth token'
