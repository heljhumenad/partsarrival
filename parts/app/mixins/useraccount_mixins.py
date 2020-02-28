from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy


class UserAccountMixins(LoginRequiredMixin):
    login_url = reverse_lazy("login")
    redirect_field_name = "next_link"
