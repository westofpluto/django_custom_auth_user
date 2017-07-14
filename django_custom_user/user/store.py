# -*- coding: utf-8
# Models
from django_custom_user.models import User


class UserStore():
    """
    User store
    """

    model = User
    query_set = User.objects

    def save(self, user):
        user.save()
        return user

    def create(self, email, username, first_name,
               last_name, password, defer=False):
        user = self.model(
            email=email,
            username=username,
            first_name=first_name,
            last_name=last_name,
            is_active=True,
            is_disabled=False)

        user.set_password(password)

        if not defer:
            user.save()

        return user
