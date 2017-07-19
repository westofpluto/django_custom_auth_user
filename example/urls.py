from django.conf.urls import url
from django.contrib import admin

from registration.views import RegisterView
from authentication.views \
    import LoginView, AuthTokenView, AuthTokenServiceView, LogoutView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^register/', RegisterView.as_view()),
    url(r'^login/', LoginView.as_view()),
    url(r'^logout/', LogoutView.as_view()),
    url(r'^auth-token/', AuthTokenView.as_view()),
    url(r'^auth-token-service/', AuthTokenServiceView.as_view()),
]
