from django.urls import path, include
from .views import RegistrationView, CustomLoginView, CustomLogoutView, VerifyEmailView

urlpatterns = [
    path('registration/', view= RegistrationView.as_view(), name= 'sign_up'),
    path(route= 'authorization/', view= CustomLoginView.as_view(), name= 'login'),
    path("logout/", view = CustomLogoutView.as_view(), name = "logout"),
    path('verify-email/', VerifyEmailView.as_view(), name='verify_email'),
]