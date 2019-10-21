from django.shortcuts import redirect, render
from django.views.generic import TemplateView


class SignUpView(TemplateView):
    template_name = 'individual/signup.html'

class LoginView(TemplateView):
    template_name = 'individual/login.html'

class HomeView(TemplateView):
    template_name = 'home.html'
