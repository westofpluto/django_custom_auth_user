# -*- coding: utf-8
# Core
from django.contrib import admin

# Models
from django_custom_user.user.model import User

# Admins
from django_custom_user.user.admin import UserAdmin


# Register admins
admin.site.register(User, UserAdmin)
