# -*- coding: utf-8
# Core
from django.contrib import admin

# Model
from django_custom_user.models import User
from django_custom_user.models import AuthToken

# Admin
from django_custom_user.user.admin import UserAdmin
from django_custom_user.auth.admin import AuthTokenAdmin


# Register admins
admin.site.register(User, UserAdmin)
admin.site.register(AuthToken, AuthTokenAdmin)
