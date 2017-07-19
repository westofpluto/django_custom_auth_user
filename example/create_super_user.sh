#!/bin/bash
echo -e "from django.contrib.auth import get_user_model;
user_model = get_user_model();
if not user_model.objects.filter(email='admin@cloud.com').exists() : user_model.objects.create_superuser('admin@cloud.com', 'password', username='admin')\n" | python manage.py shell
