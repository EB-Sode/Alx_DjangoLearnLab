from django.urls import path
from .views import RegisterView, LoginView
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path("register/", RegisterView.as_view(), name="register"),
    path("api/login/", LoginView.as_view(), name="login"),
]
