from django import forms
from django.utils.translation import ugettext_lazy as _

from parts.core import validators
from parts.app.arrival.models import PartsArrival
from parts.app.advisor.models import ServiceAdvisor
from parts.app.partsnumber.models import PartsNumber, PartNumberClass


class PartsArrivalForm(forms.ModelForm):

    advisor = forms.ModelChoiceField(
        queryset=ServiceAdvisor.objects.order_by("last_name", "first_name"),
        empty_label=_("Choose your Advisor"),
    )

    item_class = forms.ModelChoiceField(
        queryset=PartNumberClass.objects.order_by("charge_type"),
        empty_label=_("Choose your Item Class"),
    )

    reason = forms.CharField(widget=forms.Textarea(attrs={"rows":5, "cols":20}))

    class Meta:
        verbose_name = _("Parts Arrival Form")
        verbose_name_plural = _("Parts Arrival Forms")
        model = PartsArrival
        fields = [
            "customer_name",
            "ro_number",
            "item_class",
            "advisor",
            "partnumber",
            "qty",
            "remarks",
            "reason",
            "date_arrival",
        ]

    def __init__(self, *args, **kwargs):
        super(PartsArrivalForm, self).__init__(*args, **kwargs)
        instance = getattr(self, "instance", None)
        if instance and instance.id:
            self.fields["ro_number"].widget.attrs["readonly"] = True
            self.fields["customer_name"].widget.attrs["readonly"] = True
            self.fields["qty"].widget.attrs["readonly"] = True
            self.fields["partnumber"].widget.attrs["readonly"] = True
            self.fields["advisor"].widget.attrs["readonly"] = True
            self.fields["item_class"].widget.attrs["readonly"] = True
           # self.fields["date_arrival"].widget.attrs["disabled"] = True

    def clean_qty(self):
        cleaned_data = super().clean()
        qty = cleaned_data.get("qty")

        if qty < validators.DEFAULT_QTY:
            raise forms.ValidationError(
                _("Error %(qty)s quantity"), params={"qty": qty}
            )
        return qty

    def clean_ro_number(self):
        cleaned_data = super().clean()
        ro_number = cleaned_data.get("ro_number")

        if validators.DEFAULT_RO_RE_FORMAT not in ro_number:
            raise forms.ValidationError(
                _("Error %(ro_number)s not a valid format"),
                params={"ro_number": ro_number},
            )
        return ro_number
