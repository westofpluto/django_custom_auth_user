# -*- coding: utf-8
# Core
import pytest

# Models
from django_custom_user.models import User

# Store
from django_custom_user.user.store import UserStore

# Commands
from django_custom_user.user.commands.register_command import register


@pytest.mark.django_db
class TestRegisterCommand():

    @pytest.fixture
    def user_store(self):
        return UserStore()

    def test_register_command(self, user_store):
        user = register(
            user_store=user_store,
            email='email@email.com',
            username='username',
            first_name='first name',
            last_name='last name',
            password='password')

        assert isinstance(user, User), \
            'Should return user data when register command succeeds'
