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


@pytest.mark.django_db
class TestDecorators():

    def test_token_required(self):
        mixer.blend(AuthToken, token='test_token')

        @token_required
        def view(request):
            return request.user

        request = HttpRequest()
        request.META['HTTP_AUTHORIZATION'] = 'token test_token'

        try:
            response = view(request)
        except Exception:
            response = None

        assert isinstance(response, User), \
            'Should successfully authenticate token'

    def test_failed_token_required(self):

        @token_required
        def view(request):
            return request.user

        request = HttpRequest()
        request.META['HTTP_AUTHORIZATION'] = 'token test_token'

        try:
            response = view(request)
        except Http404:
            response = None

        assert response is None, 'Should fail in authenticating token'

    def test_ajax_failed_token_required(self):

        @token_required
        def view(request):
            return request.user

        request = HttpRequest()
        request.META['HTTP_AUTHORIZATION'] = 'token test_token'
        request.META['CONTENT_TYPE'] = 'application/json'
        request.META['HTTP_X_REQUESTED_WITH'] = 'XMLHttpRequest'

        try:
            response = view(request)
        except Exception:
            response = None

        assert response is None, 'Should fail in authenticating token by ajax'
