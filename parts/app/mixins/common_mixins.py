from django.contrib.auth.mixins import AccessMixin
from django.utils.translation import ugettext_lazy as _

from parts.core.mixins import MessageMixin

# Refactor this into one messages framework where you just 
# choose message and object name into MessageMixins
class CustomerMessageMixin(MessageMixin):
    success_message = _(
        "%(field)s is successfuly %(messages)s")

    def get_success_message(self, cleaned_data, **kwargs):
        return self.success_message % dict(
            cleaned_data,
            field=self.object.customer_name,
            messages=self.messages
        )


class PartsNumberMixin(MessageMixin):
    success_message = _(
        "%(field)s is successfuly %(messages)s")
    
    def get_success_message(self, cleaned_data, **kwargs):
        return self.success_message % dict(
            cleaned_data,
            field=self.object.partnumber,
            messages=self.messages
        )

class AccountsMessageMixins(MessageMixin):
    success_message = _(
            "%(field)s is successfully %(messages)s")

    def get_success_message(self, cleaned_data, **kwargs):
        return self.success_message % dict(
                cleaned_data,
                field=self.request.user,
                messages=self.messages
        )

class ServiceAdvisorMixins(MessageMixin):
    success_message = _(
            "%(field)s is successfully %(messages)s")
    
    def get_success_message(self, cleaned_data, **kwargs):
        return self.success_message % dict(
                cleaned_data,
                field=self.object.first_name,
                messages=self.messages
        )

class PartsArrivalMixins(MessageMixin):
    success_message = _(
            "%(field)s parts has been successfully %(messages)s")

    def get_success_message(self, cleaned_data, **kwargs):
        return self.success_message % dict(
                cleaned_data,
                field=self.object.customer_name,
                messages=self.messages
        )
