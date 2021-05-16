# Baseforms 
from django import forms
from django.utils.translation import gettext_lazy as _

from parts.core import validators
from parts.app.arrival.models import PartsArrival
from parts.app.advisor.models import ServiceAdvisor
from parts.app.partsnumber.models import (
        PartsNumber,
        UnitMeasure,
        PartNumberClass
)

class FormsForm(forms.ModelForm):
    pass


class PartsNumberForm(FormsForm):
    class Meta:
        verbose_name = _("Parts Number")
        verbose_name_plural = _("Parts Numbers")
        model = PartsNumber
        fields = ["partnumber",
                  "source_code",
                  "bar_code",
                  "description",
                  "unit_measure",
                  "selling_price",
        ]
        ordering = ["-id"]

    def clean_partnumber_sourcode(self):
        """
          Clean and validate input for source code and partnumber uniqueness in
          the database
          
          Input           Output                                Process
          Source Code     Validation Error when                 Get the source code and partnumber
          Partnumber      Source code and Partnumber not unique Process the validation for uniqueness
                                                                Return data from validation

        """
        cleaned_data  = super().clean()
        source_code = cleaned_data.get("source_code")
        partnumber = cleaned_data.get("partnumber")
        queryset = PartsNumber.object.filter(partnumber=partnumber, source_code=source_code)
        if queryset:
            raise form.ValidationError(
                    _("Partnumber and Source code %(partnumber)s %(source_code)s is not valid"),
                    params = {"partnumber": partnumber,
                              "source_code": source_code},
            )
        return queryset


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


class UnitofMeasureForm(forms.ModelForm):
    class Meta:
        verbose_name = _("Unit of Measure")
        verbose_name_plural = _("Unit of Measures")
        model = UnitMeasure
        fields = ["um", "description"]
        ordering = ["-id"]


class PartNumberClassForm(FormsForm):
    class Meta:
        verbose_name = _("Part Number Class")
        verbose_name_plural = _("Part Number Classes")
        model = PartNumberClass
        fields = ["charge_type", "class_name"]

    def __init__(self, *args, **kwargs):
        super(PartNumberClassForm, self).__init__(*args, **kwargs)
        instance = getattr(self, "instance", None)
        if instance and instance.id:
            self.fields["charge_type"].widget.attrs["readonly"] = True


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
        verbose_name = _("Parts Arrival Form")
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

    def __init__(self, *args, **kwargs):
        super(PartsArrivalForm, self).__init__(*args, **kwargs)
        instance = getattr(self, "instance", None)
        fields = ["ro_number", "customer_name",
                  "qty", "partnumber", "advisor",
                  "advisor","item_class"]

        if instance and instance.id:
            for field in fields:
               self.fields[field].widget.attrs["readonly"] = True
           
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
