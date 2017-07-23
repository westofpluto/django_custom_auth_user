==========
Query Sets
==========

User QuerySets
--------------

::

    # Get all users
    users = User.objects.get_all()

    # Get find user by id
    user = User.objects.find_by_id(id=1)

    # Get find usermame by id
    user = User.objects.find_by_username(username='user')

    # Get find email by id
    user = User.objects.find_by_email(email='user@cloud.com')

    # Filter active users
    users = User.objects.filter_by_active()

    # Filter inactive users
    users = User.objects.filter_by_inactive()

    # Filter enabled users
    users = User.objects.filter_by_enabled()

    # Filter disabled users
    users = User.objects.filter_by_disabled()

AuthToken QuerySets
-------------------

::

    # Get all auth token
    token = AuthToken.objects.get_all()

    # Find by id
    token = AuthToken.objects.find_by_id(id=1)

    # Find by token
    token = AuthToken.objects.find_by_token(token='token')

    # Filter by active or unexpired tokens
    token = AuthToken.objects.filter_by_active()

    # Filter by expired token
    token = AuthToken.objects.filter_by_expired()
