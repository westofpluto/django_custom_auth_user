# -*- coding: utf-8
# Core
from django.contrib import admin

# Models
from django_custom_user.auth_token.model import AuthToken

# Admin
from django_custom_user.auth_token.admin import AuthTokenAdmin


# Register admins
admin.site.register(AuthToken, AuthTokenAdmin)
