# -*- coding: utf-8
# flake8: noqa
from django.http import JsonResponse
from django.views.generic import View
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

# Token auth
from django_custom_user.auth_token.authenticate_user \
    import AuthenticateUserService
from django_custom_user.auth_token.authenticate_token \
    import AuthenticateTokenService

# Token auth decorator
from django_custom_user.auth_token.decorators import token_required

# Exception
from django_custom_user.auth_token.exceptions \
    import AuthenticationFailed

# Serializers
from authentication.serializer import AuthTokenSerializer
from .serializer import UserSerializer


class LoginView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(LoginView, self).dispatch(request, *args, **kwargs)

    def post(self, request):
        authentication_service = AuthenticateUserService(
            email_or_username=request.POST.get('email_or_username', ''),
            password=request.POST.get('password', ''))

        try:
            token = authentication_service.run()
        except AuthenticationFailed:
            errors = {
                'error': {
                    'message': 'Authentication failed'
                }
            }
            return JsonResponse(errors, safe=False, status=401)

        serialized_token = AuthTokenSerializer(token).data

        return JsonResponse({'token': serialized_token}, status=200)


class AuthTokenView(View):

    @method_decorator(csrf_exempt)
    @method_decorator(token_required)
    def dispatch(self, request, *args, **kwargs):
        return super(AuthTokenView, self).dispatch(request, *args, **kwargs)

    def post(self, request):
        serialized_user = UserSerializer(request.user).data

        return JsonResponse({'user': serialized_user}, status=200)


class AuthTokenServiceView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(AuthTokenServiceView, self).dispatch(request, *args, **kwargs)

    def post(self, request):
        authentication_service = AuthenticateTokenService(
            auth_token=request.POST.get('token', ''))

        try:
            user = authentication_service.run()
        except AuthenticationFailed:
            errors = {
                'error': {
                    'message': 'Authentication failed'
                }
            }
            return JsonResponse(errors, safe=False, status=401)

        serialized_user = UserSerializer(user).data

        return JsonResponse({'token': serialized_user}, status=200)
