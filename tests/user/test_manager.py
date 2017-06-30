# -*- coding: utf-8
# Core
import pytest
from mixer.backend.django import mixer

# Model
from django_custom_user.user.model import User


@pytest.mark.django_db
class TestUserManager():

    def test_custom_user_create(self):
        try:
            user = User.objects.create_superuser(
                email=None, password='password')
        except ValueError:
            user = None

        assert user is None, 'Should not create user without email'

        user = User.objects.create_superuser(
            email='admin@cloud.com', password='password')

        assert isinstance(user, User), 'Should create super user'

        user = User.objects.create_user(
            email='member@cloud.com', username='member')

        assert isinstance(user, User), 'Should create user'

    def test_get_all(self):
        mixer.cycle(4).blend(User)
        users = User.objects.get_all()

        assert users.count() == 4, 'Should get all user, 4'

    def test_find_by_id(self):
        mixer.blend(User, id=1)

        try:
            user_should_exist = User.objects.find_by_id(id=1)
        except User.DoesNotExist:
            user_should_exist = None

        try:
            user_should_not_exist = User.objects.find_by_id(id=3)
        except User.DoesNotExist:
            user_should_not_exist = None

        assert user_should_exist is not None, 'Should get user by id'
        assert user_should_not_exist is None, 'Should not get user by id'

    def test_find_by_username(self):
        mixer.blend(User, username='username_test')

        try:
            user_should_exist = User.objects.find_by_username(
                username='username_test')
        except User.DoesNotExist:
            user_should_exist = None

        try:
            user_should_not_exist = User.objects.find_by_username(
                username='username')
        except User.DoesNotExist:
            user_should_not_exist = None

        assert user_should_exist is not None, 'Should get user by username'
        assert user_should_not_exist is None, 'Should not get user by username'

    def test_find_by_email(self):
        mixer.blend(User, email='test_email@cloud.com')

        try:
            user_should_exist = User.objects.find_by_email(
                email='test_email@cloud.com')
        except User.DoesNotExist:
            user_should_exist = None

        try:
            user_should_not_exist = User.objects.find_by_email(
                email='email@cloud.com')
        except User.DoesNotExist:
            user_should_not_exist = None

        assert user_should_exist is not None, 'Should get user by email'
        assert user_should_not_exist is None, 'Should not get user by email'

    def test_filter_by_active(self):
        mixer.blend(User, is_active=True)
        mixer.cycle(4).blend(User)

        active_users = User.objects.filter_by_active()

        for user in active_users:
            assert user.is_active is True, 'Should get all active users'

    def test_filter_by_inactive(self):
        mixer.blend(User, is_active=False)
        mixer.cycle(4).blend(User)

        inactive_users = User.objects.filter_by_inactive()

        for user in inactive_users:
            assert user.is_active is False, 'Should get all inactive users'

    def test_filter_by_enabled(self):
        mixer.blend(User, is_disabled=False)
        mixer.cycle(4).blend(User)

        enabled_users = User.objects.filter_by_enabled()

        for user in enabled_users:
            assert user.is_disabled is False, 'Should get all enabled users'

    def test_filter_by_disbled(self):
        mixer.blend(User, is_disabled=True)
        mixer.cycle(4).blend(User)

        disabled_users = User.objects.filter_by_disabled()

        for user in disabled_users:
            assert user.is_disabled is True, 'Should get all disabled users'
