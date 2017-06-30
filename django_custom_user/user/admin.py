# -*- coding: utf-8
from django.contrib import admin

from django_custom_user.user.model import User


class UserAdmin(admin.ModelAdmin):
    pass


admin.site.register(User, UserAdmin)
