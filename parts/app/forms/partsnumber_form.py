from django import forms
from django.utils.translation import gettext_lazy as _

from parts.core import validators
from parts.app.partsnumber.models import PartsNumber, UnitMeasure


class PartsNumberForm(forms.ModelForm):
    class Meta:
        verbose_name = _("Parts Number")
        verbose_name_plural = _("Parts Numbers")
        model = PartsNumber
        fields = ["partnumber", "description", "unit_measure"]
        ordering = ["-id"]

    def clean_partnumber(self):
        # Throw and error if partnumber was not in proper format
        cleaned_data = super().clean()
        partnumber = cleaned_data.get("partnumber")

        if (
            len(partnumber) != validators.MAX_VALUE_OF_PARTNUMBER
            or len(partnumber) > validators.MAX_VALUE_OF_PARTNUMBER
        ):
            raise forms.ValidationError(
                _("Partnumber %(partnumber)s size is not valid"),
                params={"partnumber": partnumber},
            )
        return partnumber


class UnitofMeasureForm(forms.ModelForm):
    class Meta:
        verbose_name = _("Unit of Measure")
        verbose_name_plural = _("Unit of Measures")
        model = UnitMeasure
        fields = ["um"]
        ordering = ["-id"]
