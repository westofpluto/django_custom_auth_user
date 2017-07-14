# -*- coding: utf-8
# Core
import pytest

# Models
from django_custom_user.models import User

# Store
from django_custom_user.user.store import UserStore


@pytest.mark.django_db
class TestUserStore():

    @pytest.fixture
    def user_store(self):
        return UserStore()

    def test_save(self, user_store):
        user = User(email='email')
        user_store.save(user=user)

        try:
            user = User.objects.find_by_email('email')
        except User.DoesNotExist:
            user = None

        assert user, 'Should save user data in database'

    def test_create(self, user_store):
        user_store.create(
            email='email@email.com',
            username='username',
            first_name='first name',
            last_name='last name',
            password='password')

        try:
            user = User.objects.find_by_email('email@email.com')
        except User.DoesNotExist:
            user = None

        assert user, 'Should save user data in database'
