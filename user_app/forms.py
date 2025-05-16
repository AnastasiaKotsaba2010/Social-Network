from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from django.views.generic.edit import FormView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView, LogoutView

from django.utils.text import capfirst


from django.contrib.auth import get_user_model


from django import forms

UserModel = get_user_model()

# UserModel = get_user_model()
class RegisterUserForm(UserCreationForm):
    email = forms.EmailField(required=True, label='Email')
    
    class Meta:
        model = User
        fields = ('email', 'password1', 'password2')
        
class CustomAuthenticationForm(AuthenticationForm):
    email_field = forms.EmailField(required=True, label='Email')
    

    def __init__(self, request=None, *args, **kwargs):
        self.request = request
        self.user_cache = None
        # super().__init__(*args, **kwargs)

        # Set the max length and label for the "username" field.
        self.username_field = UserModel._meta.get_field(UserModel.EMAIL_FIELD)
        # username_max_length = self.email_field.max_length or 254
        # self.fields["email"].max_length = email_max_length
        # self.fields["email"].widget.attrs["maxlength"] = email_max_length
        if self.fields["email"].label is None:
            self.fields["email"].label = capfirst(self.email_field.verbose_name)
    # password = forms.CharField(widget=forms.PasswordInput(), required=True, label='Password')
    
    # class Meta:
    # model = UserModel
    
    # fields = ('password')
        
class CustomLoginViewForm(LoginView):
    template_name = 'user_app/login.html'
    form_class = CustomAuthenticationForm
    success_url = 'home'
    
    def form_valid(self, form):
        # Handle login logic here
        return super().form_valid(form)

    

        
# class LoginUserForm(AuthenticationForm):
#     email = forms.CharField(max_length=150, required=True, label='email')
#     password = forms.CharField(widget=forms.PasswordInput(), required=True, label='Password')
    
#     class Meta:
#         model = User
#         fields = ('email', 'password')
        
# class CustomLoginViewForm(LoginUserForm):
#     template_name = 'user_app/login.html'
#     form_class = LoginUserForm
#     success_url = 'home'
    
#     def form_valid(self, form):
#         # Handle login logic here
#         return super().form_valid(form)
        
    
