# -*- coding: utf-8
# Django
from functools import wraps
from django.http import Http404
from django.http import JsonResponse

# Exception
from custom_auth_user.auth_token.exceptions import AuthenticationFailed

# Services
from custom_auth_user.auth_token.authenticate_token \
    import AuthenticateTokenService


#
# Use this decorator when decorating a plain view function
#
def token_required(view_func):

    def get_token(http_authorization):
        http_authorization = http_authorization.split(' ')

        if (len(http_authorization) != 2 or
                http_authorization[0].lower() != 'token'):
            return None

        return http_authorization[1]

    @wraps(view_func)
    def decorator(request, *args, **kwargs):
        authenticate_user_service = AuthenticateTokenService(
            auth_token=get_token(
                http_authorization=request.META.get(
                    'HTTP_AUTHORIZATION', '')))

        try:
            user = authenticate_user_service.run()
        except AuthenticationFailed:
            error_context = {
                'errors': {
                    'message': 'Unauthorized',
                    'code': 401,
                }
            }

            if request.is_ajax():
                return JsonResponse(error_context, status=401)

            raise Http404

        if user:
            request.user = user

        return view_func(request, *args, **kwargs)

    return decorator

#
# Use this decorator when decorating a method of a view class
# (since a view method passes in self as first argument)
#
def token_required_method(view_method):

    def get_token(http_authorization):
        http_authorization = http_authorization.split(' ')

        if (len(http_authorization) != 2 or
                http_authorization[0].lower() != 'token'):
            return None

        return http_authorization[1]

    @wraps(view_method)
    def decorator(self, request, *args, **kwargs):
        authenticate_user_service = AuthenticateTokenService(
            auth_token=get_token(
                http_authorization=request.META.get(
                    'HTTP_AUTHORIZATION', '')))

        try:
            user = authenticate_user_service.run()
        except AuthenticationFailed:
            error_context = {
                'errors': {
                    'message': 'Unauthorized',
                    'code': 401,
                }
            }

            if request.is_ajax():
                return JsonResponse(error_context, status=401)

            raise Http404

        if user:
            request.user = user

        #
        # have to call view_method this way, passing in self as first argument
        #
        return view_method(self, request, *args, **kwargs)

    return decorator
