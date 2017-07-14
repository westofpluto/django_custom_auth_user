# -*- coding: utf-8
from datetime import datetime


class AuthenticationFailed(Exception):
    """
    Login/Authentication failed
    or
    User unauthenticated
    Authentication not provided
    """

    def __init__(self, message='Authentication Failed'):
        super(AuthenticationFailed, self).__init__(message)
        self.when = datetime.now()


class GuestOnly(Exception):
    """
    For guest or not authenticated users only
    """

    def __init__(self, message='Guest only'):
        super(GuestOnly, self).__init__(message)
        self.when = datetime.now()
