# -*- coding: utf-8
# pylint: disable=W0703
# Core
import pytest
from mixer.backend.django import mixer

# Django
from django.http import Http404
from django.http.request import HttpRequest

# Models
from django_custom_user.models import User
from django_custom_user.models import AuthToken

# Decorator
from django_custom_user.auth_token.decorators import token_required


@token_required
def view(request):
    return request.user


@pytest.mark.django_db
class TestTokenRequiredDecorator():

    def test_success(self):
        mixer.blend(AuthToken, token='test_token')

        request = HttpRequest()
        request.META['HTTP_AUTHORIZATION'] = 'token test_token'

        try:
            response = view(request)
        except Exception:
            response = None

        assert isinstance(response, User), \
            'Should successfully authenticate token'

    def test_failed(self):
        request = HttpRequest()
        request.META['HTTP_AUTHORIZATION'] = 'token test_token'

        try:
            response = view(request)
        except Http404:
            response = None

        assert response is None, 'Should fail in authenticating token'

        # Test wrong token format
        request.META['HTTP_AUTHORIZATION'] = 'test_token'

        try:
            response = view(request)
        except Http404:
            response = None

        assert response is None, \
            'Should fail in authenticating token. Wrong format'

    def test_ajax_failed(self):
        request = HttpRequest()
        request.META['HTTP_AUTHORIZATION'] = 'token test_token'
        request.META['CONTENT_TYPE'] = 'application/json'
        request.META['HTTP_X_REQUESTED_WITH'] = 'XMLHttpRequest'

        try:
            response = view(request)
        except Exception:
            response = None

        assert response.status_code == 401, \
            'Should fail in authenticating token by ajax'
