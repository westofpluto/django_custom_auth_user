# -*- coding: utf-8
# Django
from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField

# Model
from django.contrib.auth import get_user_model

# Store
from custom_auth_user.user.store import UserStore


class UserCreationForm(forms.ModelForm):
    """
    User creation form for in the admin interface
    """

    password1 = forms.CharField(
        label='Password',
        widget=forms.PasswordInput)

    password2 = forms.CharField(
        label='Password confirmation',
        widget=forms.PasswordInput,
        help_text='Confirm password')

    class Meta:
        model = get_user_model()
        fields = ('email',)

    def clean_email(self):
        email = self.cleaned_data['email']
        user_store = UserStore()

        try:
            user_store.query_set.find_by_email(email=email)
            raise forms.ValidationError(
                'Email address is already being used')
        except get_user_model().DoesNotExist:
            pass

        return email

    def clean_username(self):
        username = self.cleaned_data['username']
        user_store = UserStore()

        try:
            user_store.query_set.find_by_username(username=username)
            raise forms.ValidationError(
                'Username is already being used')
        except get_user_model().DoesNotExist:
            pass

        return username

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")

        if password1 and password2 and password1 != password2:
            raise forms.ValidationError(
                'Password confirmation didn\'t match.')

        return password2

    def save(self, commit=True):
        """
        Save user.
        """

        user = super(UserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data['password1'])

        if commit:
            user.save()

        return user


class UserChangeForm(forms.ModelForm):
    """
    User update form for in the admin interface
    """

    password = ReadOnlyPasswordHashField(
        label='Password',
        help_text='Raw passwords are not stored, '
        'so there is no way to see this user\'s password, '
        'but you can change the password using '
        '<a href=\"{}\">this form</a>.')

    class Meta:
        model = get_user_model()
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password'].help_text = \
            self.fields['password'].help_text.format('../password/')

        f = self.fields.get('user_permissions')

        if f is not None:
            f.queryset = f.queryset.select_related('content_type')

    def clean_password(self):
        return self.initial['password']
