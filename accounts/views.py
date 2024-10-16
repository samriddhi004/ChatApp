from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
# Create your views here.

class CustomLoginView(LoginView):
    template_name="accounts/login.html"
    success_url = reverse_lazy("chat")
    
    def get_success_url(self):
        return self.success_url


class SignUpView(CreateView):
    template_name="accounts/signup.html"
    form_class = UserCreationForm
    success_url = reverse_lazy("login") #where URLs might not be immediately available at the time of class definition or settings evaluation.