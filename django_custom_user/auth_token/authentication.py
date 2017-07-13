# -*- coding: utf-8
# Stores
from django_custom_user.auth.store import AuthTokenStore


class TokenAuthenticationService():
    """
    Token authentication service
    """

    auth_token_store = AuthTokenStore()

    def __init__(self, email_or_username, password):
        self.email_or_username = email_or_username
        self.password = password

    def run(self):
        pass
