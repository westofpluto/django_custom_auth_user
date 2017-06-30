# -*- coding: utf-8
from django.utils import timezone
from django.db import models
from django_custom_user.user.model import User
from django_custom_user.auth_token.manager import AuthTokenManager


class AuthToken(models.Model):

    token = models.CharField(max_length=255, unique=True)
    expiration_date = models.DateTimeField(
        default=timezone.now() + timezone.timedelta(days=1))
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='auth_tokens')
    created_at = models.DateTimeField(auto_now_add=True)

    objects = AuthTokenManager()

    def __str__(self):
        return self.token + ' - ' + self.user.username
