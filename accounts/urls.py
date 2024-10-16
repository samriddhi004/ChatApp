from django.urls import path
from django.contrib.auth.views import LoginView
from .views import SignUpView,CustomLoginView

urlpatterns = [
    path("login/",CustomLoginView.as_view(),name="login"),
    path("signup/",SignUpView.as_view(),name="signup")
]
