# -*- coding: utf-8
# Core
import serpy

# Serializers
from registration.serializer import UserSerializer


class AuthTokenSerializer(serpy.Serializer):

    id = serpy.IntField(
        attr='id',
        required=True)

    token = serpy.StrField(
        attr='token',
        required=True)

    user = UserSerializer()

    created_at = serpy.StrField(
        attr='created_at',
        required=False)

    expiration_date = serpy.StrField(
        attr='expiration_date',
        required=False)
