# -*- coding: utf-8
from django.contrib import admin

# Models
from django_custom_user.auth_token.model import AuthToken


@admin.register(AuthToken)
class AuthTokenAdmin(admin.ModelAdmin):
    pass
