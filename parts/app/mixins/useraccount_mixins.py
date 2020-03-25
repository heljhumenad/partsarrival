from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.translation import ugettext_lazy as _
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy


class UserAccountMixins(LoginRequiredMixin):
    login_url = reverse_lazy("login")
    redirect_field_name = "next_link"


class MessageMixins(LoginRequiredMixin, SuccessMessageMixin):
    @property
    def messages(self):
        return NotImplemented


class UserSuccessMessageMixin(MessageMixins):
    success_message = _(
        "%(customer_name)s is successfuly %(messages)s")

    def get_success_message(self, cleaned_data, **kwargs):
        return self.success_message % dict(
            cleaned_data,
            customer_name=self.object.customer_name,
            messages=self.messages
        )


class PartsNumberMixin(MessageMixins):
    success_message = _(
        "%(partnumber)s is successfuly %(messages)s"
    )

    def get_success_message(self, cleaned_data, **kwargs):
        return self.success_message % dict(
            cleaned_data,
            partnumber=self.object.partnumber,
            messages=self.messages
        )
