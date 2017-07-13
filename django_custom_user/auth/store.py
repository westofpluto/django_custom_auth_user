# -*- coding: utf-8
# Models
from django_custom_user.models import AuthToken


class AuthTokenStore():

    model = AuthToken

    def save(self, auth_token):
        auth_token.save()
        return auth_token
