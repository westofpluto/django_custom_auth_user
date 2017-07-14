# -*- coding: utf-8
# Models
from django_custom_user.models import User


def authenticate_user(user_store, email_or_username, password):
    user_query = user_store.query_set.filter_by_active().filter_by_enabled()

    # Try finding user by username first
    try:
        user = user_query.find_by_username(email_or_username)
    except User.DoesNotExist:
        user = None

    # If username does not exist try finding by email
    if user is None:
        try:
            user = user_query.find_by_email(email_or_username)
        except User.DoesNotExist:
            user = None

    # If no user return 'None'
    if user is None:
        return None

    # Check user if match password, else return 'None'
    if user.check_password(password) is False:
        return None

    return user
