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

    # date_arrival = forms.DateTimeField(
    #     input_formats='%m/%d/%Y %H:%M',
    #     localize=True
    # )

    class Meta:
        verbose_name = _("Parts Arrival Form")
        verbose_name_plural = _("Parts Arrival Forms")
        model = PartsArrival
        fields = [
            'customer_name', 'ro_number',
            'item_class', 'advisor',
            'partnumber', 'qty',
            'remarks', 'date_arrival',
        ]

    def __init__(self, *args, **kwargs):
        super(PartsArrivalForm, self).__init__(*args, **kwargs)
        instance = getattr(self, "instance", None)
        if instance and instance.id:
            self.fields["ro_number"].widget.attrs["readonly"] = True
            self.fields["customer_name"].widget.attrs["readonly"] = True
            self.fields["qty"].widget.attrs["readonly"] = True

    def clean_qty(self):
        # check input qty if zero
        cleaned_data = super().clean()
        qty = cleaned_data.get("qty")

        if qty <= 0 or qty is None:
            raise forms.ValidationError(
                _("Error %(qty)s quantity"),
                params={'qty': qty},
            )
        return qty

    def clean_ro_number(self):
        cleaned_data = super().clean()
        ro_number = cleaned_data.get("ro_number")

        if "RO" not in ro_number:
            raise forms.ValidationError(
                _("Error %(ro_number)s not a valid format"),
                params={'ro_number': ro_number},
            )
        return ro_number
