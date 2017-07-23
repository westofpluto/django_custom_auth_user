# -*- coding: utf-8
# Core
import pytest

# Models
from custom_auth_user.models import User

# Store
from custom_auth_user.user.store import UserStore

# Commands
from custom_auth_user.auth_token.commands.authenticate_user_command \
    import authenticate_user


@pytest.mark.django_db
class TestAuthenticateUserCommand():

    @pytest.fixture
    def user_store(self):
        return UserStore()

    def test_authenticate_user_command(self, user_store):
        User.objects.create_superuser(
            email='email@email.com',
            password='emailpassword')
        User.objects.create_superuser(
            email='email@cloud.com',
            password='userpassword',
            username='username')

        not_authenticate = authenticate_user(
            user_store=user_store,
            email_or_username='invalid',
            password='invalidpassword')

        assert not_authenticate is None, 'Should not be authenticated'

        username_authenticate = authenticate_user(
            user_store=user_store,
            email_or_username='username',
            password='userpassword')

        assert username_authenticate, 'Should be authenticated by username'

        email_authenticate = authenticate_user(
            user_store=user_store,
            email_or_username='email@email.com',
            password='emailpassword')

        assert email_authenticate, 'Should be authenticated by email'
