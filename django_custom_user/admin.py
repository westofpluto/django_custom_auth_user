# -*- coding: utf-8
# Core
from django.contrib import admin

# Model
from django_custom_user.user.model import User

# Admin
from django_custom_user.user.admin import UserAdmin


# Register admins
admin.site.register(User, UserAdmin)
