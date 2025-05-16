from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView
from django.contrib.auth.views import LoginView, LogoutView
from .forms import RegisterUserForm, CustomLoginViewForm
from django.urls import reverse_lazy


# Create your views here.
class RegistrationView(CreateView):
    form_class = RegisterUserForm
    template_name = 'user_app/sign_up.html'
    success_url = reverse_lazy('login')
    
class CustomLoginView(CustomLoginViewForm):
    template_name ='user_app/login.html'
        
class CustomLogoutView(LogoutView):
    next_page = 'login'