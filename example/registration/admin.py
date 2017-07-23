# -*- coding: utf-8
# Core
from django.contrib import admin

# Models
from registration.models import User


# Register admins
admin.site.register(User)
