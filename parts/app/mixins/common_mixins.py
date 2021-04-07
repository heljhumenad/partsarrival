from django.contrib.auth.mixins import AccessMixin
from django.utils.translation import ugettext_lazy as _

from parts.core.mixins import MessageMixin

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
