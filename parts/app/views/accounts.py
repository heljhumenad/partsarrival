from django.views import generic
from django.contrib.auth import views
from django.urls import reverse_lazy
from django.contrib.auth import views 

from parts.app.accounts import forms
from parts.app.accounts.models import CustomUser
from parts.app.mixins.common_mixins import AccountsMessageMixins


class AccountTemplateView(generic.TemplateView):
    template_name = "accounts/index.html"


class AccountLoginView(views.LoginView):
    template = "accounts/login.html"


# TODO
# Fix Logout that can use to redirect logout without authentication
class AccountLogoutView(views.LogoutView):
    template_name = "registration/logout.html"


class AccountEditView(AccountsMessageMixins, generic.UpdateView):
    template_name = "accounts/update_user.html"
    success_url = reverse_lazy("dashboard:dashboard_view_index")
    context_object_name = "user"
    messages = 'updated'
    form_class = forms.CustomUserChangeForm

    def get_object(self, query_pk_and_slug=None):
        user = CustomUser.objects.filter(id=self.kwargs["pk"]).first()
        return user


# TODO fix bug updating password from other account
class AccountChangePasswordView(views.PasswordChangeView):
    template_name = "accounts/password_change.html"
    success_url = reverse_lazy("accounts:edit_user")
    form_class = forms.AccountPasswordChangeForm
