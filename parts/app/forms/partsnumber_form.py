from django import forms
from django.utils.translation import gettext_lazy as _

from parts.app.partsnumber.models import PartsNumber

class PartsNumberForm(forms.ModelForm):
    
    class Meta:
        verbose_name = _("Parts Number")
        verbose_name_plural = _("Parts Numbers")
        model = PartsNumber
        fields = [
                'partnumber',
                'unit_measure',
                'description',
                ]
        ordering = ['-id']
