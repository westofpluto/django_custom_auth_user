# -*- coding: utf-8
from django.contrib.auth.admin import UserAdmin

# Forms
from custom_auth_user.user.forms.admin_user_forms import UserCreationForm
from custom_auth_user.user.forms.admin_user_forms import UserChangeForm


class UserAdmin(UserAdmin):
    """
    User admin
    """

    fieldsets = (
        (None, {'fields': ('email', 'username', 'password')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser',
                                    'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'username', 'password1', 'password2')
        }),
    )

    form = UserChangeForm
    add_form = UserCreationForm

    list_display = ('email', 'username', 'is_staff')
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'groups')
    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ('groups', 'user_permissions',)
