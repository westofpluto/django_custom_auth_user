# -*- coding: utf-8
from django.contrib import admin

from django_custom_user.auth_token.model import AuthToken


class AuthTokenAdmin(admin.ModelAdmin):
    pass


admin.site.register(AuthToken, AuthTokenAdmin)
