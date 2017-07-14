from django.conf.urls import url
from django.contrib import admin

from example.registration.views import RegisterView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^register/', RegisterView.as_view()),
]
