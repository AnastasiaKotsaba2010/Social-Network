# from django.contrib.auth.forms import UserCreationForm 
from django.views.generic.edit import CreateView
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy

from .forms import CustomUserCreationForm, EmailAuthenticationForm
from django.shortcuts import redirect
from django.core.mail import send_mail
from .models import EmailConfirmation, User

from django.views import View
from django.shortcuts import render


# Create your views here.


class RegistrationView(CreateView):
    form_class = CustomUserCreationForm 
    template_name = "user_app/sign_up.html" 
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        user = form.save()
        code_entry, _ = EmailConfirmation.objects.get_or_create(user=user)
        code_entry.generate_code()

        send_mail(
            subject='Підтвердження електронної пошти',
            message=f"Ваш код підтвердження: {code_entry.code}",
            from_email='worldIT@gmail.com',
            recipient_list=[user.email],
        )

        self.request.session['pending_user_id'] = user.id
        return redirect('verify_email')
    
    def get_context_data(self, **kwargs):
        context=  super().get_context_data(**kwargs)
        context['form_name'] = 'register'
        return context
    
class CustomLoginView(LoginView):
    form_class = EmailAuthenticationForm
    template_name = 'user_app/login.html'
    
    def get_context_data(self, **kwargs):
        context=  super().get_context_data(**kwargs)
        context['form_name'] = 'auth'
        return context
    
class CustomLogoutView(LogoutView):
    next_page = 'login'


class VerifyEmailView(View):
    template_name = 'user_app/verify_email.html'

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        input_code = ''.join([request.POST.get(f'code{i}', '') for i in range(6)])
        user_id = request.session.get('pending_user_id')
        if not user_id:
            return redirect('sign_up')

        try:
            confirmation = EmailConfirmation.objects.get(user_id=user_id)
        except EmailConfirmation.DoesNotExist:
            return redirect('sign_up')

        if confirmation.code == input_code:
            confirmation.delete()
            del request.session['pending_user_id']
            return redirect('login')
        else:
            return render(request, self.template_name, {'error': 'Код неправильний'})
