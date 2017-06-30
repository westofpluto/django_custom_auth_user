# -*- coding: utf-8
from django_custom_user.auth_token.model import AuthToken
from django.utils.crypto import get_random_string


class AuthTokenService():

    def create(self, user):
        auth_token = AuthToken(
            token=self.generate_token(),
            user=user)
        auth_token.save()

        return auth_token

    def generate_token(self, token=None):
        if token is None:
            token = get_random_string(32)

        try:
            AuthToken.objects.select_related('user').find_by_token(token)

            return self.generate_token()
        except AuthToken.DoesNotExist:
            return token
