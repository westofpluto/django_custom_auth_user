# -*- coding: utf-8
# Core
import pytest

# Exception
from custom_auth_user.user.exceptions import InvalidInput

# Service
from custom_auth_user.user.registration import RegistrationService

# Model
from custom_auth_user.models import User


@pytest.mark.django_db
class TestRegistrationService():

    def test_registration_service(self):
        registration_service = RegistrationService(
            email='', username='', first_name='', last_name='', password='')

        registration_form_errors = {}

        try:
            registration_service.run()
        except InvalidInput:
            registration_form_errors = \
                registration_service.get_registration_form_errors()

        assert registration_form_errors, 'Should have invalid form errors'

        registration_service = RegistrationService(
            email='email@email.com',
            username='username',
            first_name='first name',
            last_name='last name',
            password='password')

        user_data = registration_service.run()

        assert isinstance(user_data, User), \
            'Should return user data when register service succeeds'
