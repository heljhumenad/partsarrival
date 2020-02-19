from django import forms
from django.utils.translation import ugettext_lazy as _

from parts.app.partsnumber.models import PartNumberClass


class PartNumberClassForm(forms.ModelForm):

    class Meta:
        verbose_name = _("Part Number Class")
        verbose_name_plural = _("Part Number Classes")
        model = PartNumberClass
        fields = ['code_name', 'charge_type', 'class_name']
