# -*- coding: utf-8
# Core
import pytest
from mixer.backend.django import mixer

# Models
from django_custom_user.models import User

# Stores
from django_custom_user.user.store import UserStore

# Forms
from django_custom_user.user.forms.registration_form import RegistrationForm


@pytest.mark.django_db
class TestRegistrationForm():

    @pytest.fixture
    def user_store(self):
        return UserStore()

    def test_email(self, user_store):
        form = RegistrationForm(user_store=user_store, data={'email': ''})
        assert form.errors['email'][0] == 'Email address is required', \
            'Should fail if email is blank'

        form = RegistrationForm(
            user_store=user_store, data={'email': 'invalid@email'})
        assert form.errors['email'][0] == 'Email address is invalid', \
            'Should fail if email is invalid'

        mixer.blend(User, email='email@cloud.com')
        form = RegistrationForm(
            user_store=user_store, data={'email': 'email@cloud.com'})
        assert form.errors['email'][0] == \
            'Email address is already being used', \
            'Should fail if email is already existed'

        form = RegistrationForm(
            user_store=user_store, data={'email': 'valid@email.com'})
        assert form.errors.get('email') is None, 'Should be a valid email'

    def test_username(self, user_store):
        form = RegistrationForm(user_store=user_store, data={'username': ''})
        assert form.errors['username'][0] == 'Username is required', \
            'Should fail if username is blank'

        form = RegistrationForm(
            user_store=user_store, data={'username': '!@#_A'})
        assert form.errors['username'][0] == \
            'Usernames can only contain lowercase letters, \
                numbers, periods, hyphens, and underscores', \
            'Should fail if username is invalid'

        mixer.blend(User, username='test_username')
        form = RegistrationForm(
            user_store=user_store, data={'username': 'test_username'})
        assert form.errors['username'][0] == \
            'Username is already being used', \
            'Should fail if username is already existed'

        form = RegistrationForm(
            user_store=user_store, data={'username': 'username'})
        assert form.errors.get('username') is None, \
            'Should be a valid username'

    def test_first_name(self, user_store):
        form = RegistrationForm(
            user_store=user_store, data={'first_name': ''})
        assert form.errors['first_name'][0] == 'First name is required', \
            'Should fail if first name is blank'

        form = RegistrationForm(
            user_store=user_store, data={'first_name': 'first name'})
        assert form.errors.get('first_name') is None, \
            'Should be a valid first name'

    def test_last_name(self, user_store):
        form = RegistrationForm(user_store=user_store, data={'last_name': ''})
        assert form.errors['last_name'][0] == 'Last name is required', \
            'Should fail if last name is blank'

        form = RegistrationForm(
            user_store=user_store, data={'last_name': 'last name'})
        assert form.errors.get('last_name') is None, \
            'Should be a valid last name'

    def test_password(self, user_store):
        form = RegistrationForm(user_store=user_store, data={'password': ''})
        assert form.errors['password'][0] == 'Password is required', \
            'Should fail if password is blank'

        form = RegistrationForm(
            user_store=user_store, data={'password': 'short'})
        assert form.errors['password'][0] == \
            'Password must be at least 6 characters', \
            'Should fail if password is short'

        form = RegistrationForm(
            user_store=user_store, data={'password': 'password'})
        assert form.errors.get('password') is None, \
            'Should be a valid password'

    def test_form(self, user_store):
        form = RegistrationForm(user_store=user_store, data={
            'email': 'email@cloud.com',
            'username': 'username',
            'first_name': 'first name',
            'last_name': 'last name',
            'password': 'password'})

        assert form.is_valid() is True, 'Should be valid form entries'
