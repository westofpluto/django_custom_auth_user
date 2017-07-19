# -*- coding: utf-8
# flake8: noqa: F401
# Core
import pytest

# Django
from django.contrib.admin.sites import AdminSite
from django.contrib.admin.options import ModelAdmin

# Models
from custom_auth_user.models import User

# Admins
from custom_auth_user.admin import *


class MockRequest:
    pass


request = MockRequest()


@pytest.mark.django_db
class TestUserAdmin():

    @pytest.fixture
    def user_model_admin(self):
        return ModelAdmin(User, AdminSite())

    def test_user_admin(self, user_model_admin):
        assert str(user_model_admin) == 'custom_auth_user.ModelAdmin'

    def test_user_admin_fields(self, user_model_admin):
        admin_fields = set(list(user_model_admin.get_fields(request)))
        admin_fields_compare = set(['password', 'email', 'username',
                                    'first_name', 'last_name', 'is_staff',
                                    'is_active', 'is_disabled', 'date_joined',
                                    'last_login', 'is_superuser', 'groups',
                                    'user_permissions'])

        assert len(admin_fields) == len(admin_fields_compare)

        assert admin_fields == admin_fields_compare
