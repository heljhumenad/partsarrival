from django import forms
from django.utils.translation import ugettext_lazy as _

from parts.app.arrival.models import PartsArrival
from parts.app.advisor.models import ServiceAdvisor
from parts.app.partsnumber.models import (PartsNumber, PartNumberClass)


class PartsArrivalForm(forms.ModelForm):

    advisor = forms.ModelChoiceField(
        queryset=ServiceAdvisor.objects.all(),
        empty_label=_("Choose your Advisor")
    )

    item_class = forms.ModelChoiceField(
        queryset=PartNumberClass.objects.all(),
        empty_label=_("Choose your Item Class")
    )

    partnumber = forms.ModelChoiceField(
        queryset=PartsNumber.objects.all(),
        empty_label=_("Choose your Partnumber")
    )

    class Meta:
        verbose_name = _("Parts Arrival Form")
        verbose_name_plural = _("Parts Arrival Forms")
        model = PartsArrival
        fields = [
            'customer_name', 'ro_number',
            'item_class', 'advisor',
            'partnumber', 'description',
            'qty', 'remarks', 'date_arrival',
        ]
