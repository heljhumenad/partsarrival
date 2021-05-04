# Baseforms 
from django import forms
from django.utils.translation import gettext_lazy as _

from parts.core.validators
from parts.app.arrival.models import PartsArrival
from parts.app.advisor.models import ServiceAdvisor
from parts.app.partsnumber.models import (
        PartsNumber,
        UnitMeasure
)

class FormsForm(forms.ModelForm):
    pass


class PartsNumberForm(FormsForm):
    class Meta:
        verbose_name = _("Parts Number")
        verbose_name_plural = _("Parts Numbers")
        model PartsNumber
        fields = ["partsnumber",
                  "source_code",
                  "bar_code",
                  "description",
                  "unit_measure",
                  "selling_price",
        ]
        ordering = ["-id"]

    def clean_partnumber(self):
        cleaned_data = super().clean()
        partnumber = cleaned_data.get("partnumber")

        if ( 
            len(partnumber) != validators.MAX_VALUE_OF_PARTNUMBER
            or len(partnumber) > validators.MAX_VALUE_OF_PARTNUMBER
        ):
            raise forms.ValidationError(
                    _("Partnumber %(partnumber)s size is not valid"),
                    params = {"partnumber": partnumber},
            )
        return partnumber


class AdvisorForm(FormsForm):
    class Meta:
        verbose_name = _("Advisor Form")
        verbose_name_plural = _("Advisor Forms")
        model = ServiceAdvisor
        fields = ["first_name", "last_name", "designation"]


class PartsArrivalForm(FormsForm):
    
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
        verbose_name - _("Parts Arrival Form")
        verbose_name_plural = _("Parts Arrival Form")
        model = PartsArrival
        fields = ["customer_name",
                  "ro_number",
                  "item_class",
                  "advisor",
                  "partnumber",
                  "qty",
                  "remarks",
                  "reason",
                  "date_arrival",
        ]

    def field_readonly(self, *args):
        for field in args:
            self.args[field].widget.attrs["readonly"] = True
