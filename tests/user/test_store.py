# -*- coding: utf-8
# Core
import pytest
from mixer.backend.django import mixer

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

    def test_find_by_email(self, user_store):
        mixer.blend(User, email='test_email@cloud.com')

        try:
            user_should_exist = user_store.find_by_email(
                email='test_email@cloud.com')
        except User.DoesNotExist:
            user_should_exist = None

        try:
            user_should_not_exist = user_store.find_by_email(
                email='email@cloud.com')
        except User.DoesNotExist:
            user_should_not_exist = None

        assert user_should_exist is not None, 'Should get user by email'
        assert user_should_not_exist is None, 'Should not get user by email'

    def test_find_by_username(self, user_store):
        mixer.blend(User, username='test_username')

        try:
            user_should_exist = user_store.find_by_username(
                username='test_username')
        except User.DoesNotExist:
            user_should_exist = None

        try:
            user_should_not_exist = user_store.find_by_username(
                username='username')
        except User.DoesNotExist:
            user_should_not_exist = None

        assert user_should_exist is not None, 'Should get user by username'
        assert user_should_not_exist is None, 'Should not get user by username'
