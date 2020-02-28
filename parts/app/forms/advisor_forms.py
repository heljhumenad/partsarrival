from django import forms
from django.utils.translation import ugettext_lazy as _
from parts.app.advisor.models import ServiceAdvisor

class AdvisorForm(forms.ModelForm):
    
    class Meta:
        verbose_name = _("Advisor Form")
        verbose_name_plural = _("Advisors Forms")
        model = ServiceAdvisor
        fields = ['first_name', 'last_name', 'designation']
