from django.views import generic
from django.utils.translation import ugettext_lazy as _
from django.urls import reverse_lazy


from parts.app.mixins.useraccount_mixins import UserSuccessMessageMixin


class UserCreateViewMixins(UserSuccessMessageMixin, generic.CreateView):
    messages = 'added'


class UserUpdateViewMixins(UserSuccessMessageMixin, generic.UpdateView):
    messages = 'updated'
