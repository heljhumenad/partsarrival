from django.contrib.auth.mixins import AccessMixin, LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.utils.translation import gettext as _


class MessageMixin(LoginRequiredMixin, SuccessMessageMixin):
    login_url = reverse_lazy("login")
    redirect_field_name = "next_link"
    
    @property
    def messages(self):
        return NotImplemented
