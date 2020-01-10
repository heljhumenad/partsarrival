from django.views import generic
from django.contrib.auth import views
from django.urls import reverse_lazy

class AccountTemplateView(generic.TemplateView):
    template_name = 'accounts/index.html'

class AccountLoginView(views.LoginView):
    template = 'accounts/login.html'

class AccountLogoutView(views.LogoutView):
    template_name = 'registration/logout.html'
    next_page = reverse_lazy('accounts:login')
    redirect_field_name = 'next'
