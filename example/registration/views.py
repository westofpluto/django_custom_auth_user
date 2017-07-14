# -*- coding: utf-8
# flake8: noqa
import json
from django.core import serializers
from django.http import HttpResponse
from django.views.generic import View
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

# Custom User
from django_custom_user.user.registration import RegistrationService

# Exception
from django_custom_user.user.exceptions import InvalidInput


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
            return HttpResponse(
                json.dumps({
                    'error': registration_service.get_registration_form_errors()}),
                content_type='application/json')

        serialized_user = serializers.serialize('json', [user])

        return HttpResponse(
            json.dumps({'user': serialized_user}),
            content_type='application/json')
