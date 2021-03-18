from django import forms
from django.utils.translation import ugettext_lazy as _
from parts.app.advisor.models import ServiceAdvisor


class AdvisorForm(forms.ModelForm):
    class Meta:
        verbose_name = _("Advisor Form")
        verbose_name_plural = _("Advisors Forms")
        model = ServiceAdvisor
        fields = ["first_name", "last_name", "designation"]
    
    def __init__(self, *args, **kwargs):
        super(AdvisorForm, self).__init__(*args, **kwargs)
    
    def clean_first_name(self):
       cleaned_data = super().clean()
       first_name = cleaned_data.get("first_name")
       queryset = ServiceAdvisor.objects.filter(first_name=first_name)

       if queryset:
           raise forms.ValidationError(
               _("Error %(first_name)s has already in database"),
               params = {"first_name": first_name},
        )
       return first_name