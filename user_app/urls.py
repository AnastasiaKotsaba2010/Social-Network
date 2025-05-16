from django.urls import path
from .views import *

urlpatterns = [
    path('sign_up/', RegistrationView.as_view(), name='sign_up'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout')
]