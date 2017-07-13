# -*- coding: utf-8
# Core
import pytest
from mixer.backend.django import mixer

# Models
from django_custom_user.models import User


@pytest.mark.django_db
class TestUserModel():

    def test_user_model(self):
        user = mixer.blend(User, first_name='first', last_name='last')

        assert isinstance(user, User), 'Should create new user instance'

        assert user.get_full_name() == 'first last', \
            'Should full name, "{first_name} {last_name}" format'

        assert user.get_short_name() == 'first', \
            'Should get short name, "{first_name}" format'
