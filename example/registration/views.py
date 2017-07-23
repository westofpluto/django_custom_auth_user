# -*- coding: utf-8
# flake8: noqa
from django.http import JsonResponse
from django.views.generic import View
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

# Custom User
from custom_auth_user.user.registration import RegistrationService

# Exception
from custom_auth_user.user.exceptions import InvalidInput

# Serializer
from .serializer import UserSerializer


class RegisterView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(RegisterView, self).dispatch(request, *args, **kwargs)

    def post(self, request):
        registration_service = RegistrationService(
            email=request.POST.get('email', ''),
            username=request.POST.get('username', ''),
            first_name=request.POST.get('first_name', ''),
            last_name=request.POST.get('last_name', ''),
            password=request.POST.get('password', ''))

        try:
            user = registration_service.run()
        except InvalidInput:
            errors = {
                'error': registration_service.get_registration_form_errors()
            }
            return JsonResponse(errors, safe=False, status=422)

        serialized_user = UserSerializer(user).data

        return JsonResponse({'user': serialized_user}, status=200)
