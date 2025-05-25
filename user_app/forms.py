from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
# from .models import CustomUser

User = get_user_model()


class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(
        label='Електронна пошта',
        max_length=75,
        required=True,
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control',
                'placeholder': "you@example.com"
            }
        )
    )
    
    password1 = forms.CharField(
        label= "Пароль", 
        required= True,
        widget= forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': "Введи пароль"
            }
        )
    )
    
    password2 = forms.CharField(
        label= "Підтверди пароль", 
        required= True,
        widget= forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': "Повтори пароль"
            }
        )
    )

    class Meta:
        model = User
        fields = ('email', 'password1', 'password2')

    def clean_email(self):
        email = self.cleaned_data["email"]
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Ця електронна пошта вже використовується.")
        return email


    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        user.email = self.cleaned_data["email"]
        user.is_active = True
        if commit:
            user.save()
        return user

class EmailAuthenticationForm(AuthenticationForm):
    username = forms.EmailField(
        label="Електронна пошта",
        widget=forms.EmailInput(
            attrs={
                "placeholder": "you@example.com",
                "class": "form-control",
                "autofocus": True,
            }
        ),
    )
    password = forms.CharField(
        label="Пароль",
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Пароль",
                "class": "form-control",
            }
        ),
    )

    field_order = ["username", "password"]
    


# class CustomUserCreationForm(UserCreationForm):
#     email = forms.EmailField(
#         label= "Електронна пошта", 
#         required= True,
#         widget= forms.EmailInput(
#             attrs={
#                 'class': 'form-control',
#                 'placeholder': "you@example.com"
#             }
#         )
#     )
     
#     password1 = forms.CharField(
#         label= "Пароль", 
#         required= True,
#         widget= forms.PasswordInput(
#             attrs={
#                 'class': 'form-control',
#                 'placeholder': "Введи пароль"
#             }
#         )
#     )
    
#     password2 = forms.CharField(
#         label= "Підтверди пароль", 
#         required= True,
#         widget= forms.PasswordInput(
#             attrs={
#                 'class': 'form-control',
#                 'placeholder': "Повтори пароль"
#             }
#         )
#     )

#     class Meta:
#         model = User
#         fields = ('email', 'password1', 'password2')
    
#     def save(self, commit=True):
#         user = super(UserCreationForm, self).save(commit=False)
#         user.email = self.cleaned_data["email"]
#         if commit:
#             user.save()
#         return user
        
#     # def __init__(self, *args, **kwargs): 
#     #     super(CustomUserCreationForm, self).__init__(*args, **kwargs) 
        
#     # def save(self):
#     #     self.instance.username = 'Nastya'
#     #     return super(CustomUserCreationForm, self).save()
    
#     def clean_username(self):
#         """Reject usernames that differ only in case."""
#         username = self.cleaned_data.get("email")
#         if (
#             username
#             and self._meta.model.objects.filter(username__iexact=username).exists()
#         ):
#             self._update_errors(
#                 ValidationError(
#                     {
#                         "username": self.instance.unique_error_message(
#                             self._meta.model, ["username"]
#                         )
#                     }
#                 )
#             )
#         else:
#             return username
#     class Meta:
#         model = UserCreationForm.Meta.model
#         fields = ("email", 'password1', 'password2')
#         field_classes = {"email": forms.EmailField}

#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         if self._meta.model.EMAIL_FIELD in self.fields:
#             self.fields[self._meta.model.EMAIL_FIELD].widget.attrs[
#                 "autofocus"
#             ] = True


    




    
