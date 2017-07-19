# -*- coding: utf-8
# Core
import serpy


class UserSerializer(serpy.Serializer):

    id = serpy.IntField(
        attr='id',
        required=True)

    email = serpy.StrField(
        attr='email',
        required=False)

    username = serpy.StrField(
        attr='username',
        required=False)

    first_name = serpy.StrField(
        attr='first_name',
        required=False)

    last_name = serpy.StrField(
        attr='last_name',
        required=False)

    last_login = serpy.StrField(
        attr='last_login',
        required=False)

    is_disabled = serpy.StrField(
        attr='is_disabled',
        required=False)
