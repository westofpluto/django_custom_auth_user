# -*- coding: utf-8
# flake8: noqa: F401
# Core
import pytest

# Django
from django.contrib.admin.sites import AdminSite
from django.contrib.admin.options import ModelAdmin

# Models
from django_custom_user.models import AuthToken

# Admins
from django_custom_user.admin import *


class MockRequest:
    pass


request = MockRequest()


@pytest.mark.django_db
class TestAuthTokenAdmin():

    @pytest.fixture
    def auth_token_model_admin(self):
        return ModelAdmin(AuthToken, AdminSite())

    def test_user_admin(self, auth_token_model_admin):
        assert str(auth_token_model_admin) == 'django_custom_user.ModelAdmin'

    def test_user_admin_fields(self, auth_token_model_admin):
        admin_fields = set(list(auth_token_model_admin.get_fields(request)))
        admin_fields_compare = set(['token', 'expiration_date', 'user'])

        assert len(admin_fields) == len(admin_fields_compare)

        assert admin_fields == admin_fields_compare