from django.views import generic
from django.contrib.auth import views
from django.urls import reverse_lazy

from parts.app.mixins.useraccount_mixins import UserAccountMixins


class AccountTemplateView(UserAccountMixins, generic.TemplateView):
    template_name = "accounts/index.html"


class AccountLoginView(views.LoginView):
    template = "accounts/login.html"

# TODO 
# Fix Logout that can use to redirect logout without authentication
class AccountLogoutView(views.LogoutView):
    template_name = "registration/logout.html"
   # next_page = reverse_lazy("accounts:login")
    redirect_field_name = "next"

