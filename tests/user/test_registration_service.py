# -*- coding: utf-8
# Core
import pytest

# Exception
from django_custom_user.user.exceptions import InvalidInput

# Service
from django_custom_user.user.registration import RegisterService

# Model
from django_custom_user.models import User


@pytest.mark.django_db
class TestRegistrationService():

    def test_registration_service(self):
        register_service = RegisterService(
            email='', username='', first_name='', last_name='', password='')

        registration_form_errors = {}

        try:
            register_service.run()
        except InvalidInput:
            registration_form_errors = \
                register_service.get_registration_form_errors()

        assert registration_form_errors, 'Should have invalid form errors'

        register_service = RegisterService(
            email='email@email.com',
            username='username',
            first_name='first name',
            last_name='last name',
            password='password')

        user_data = register_service.run()

        assert isinstance(user_data, User), \
            'Should return user data when register service succeeds'
