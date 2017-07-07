# -*- coding: utf-8
from django.contrib import admin

# Models
from django_custom_user.user.model import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    """
    User admin
    """
    pass
