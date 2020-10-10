from django import forms
from django.utils.translation import gettext_lazy as _

from parts.app.partsnumber.models import PartsNumber, UnitMeasure


class PartsNumberForm(forms.ModelForm):
    class Meta:
        verbose_name = _("Parts Number")
        verbose_name_plural = _("Parts Numbers")
        model = PartsNumber
        fields = [
            "partnumber",
            "description",
            "unit_measure",
        ]
        ordering = ["-id"]


class UnitofMeasureForm(forms.ModelForm):
    class Meta:
        verbose_name = _("Unit of Measure")
        verbose_name_plural = _("Unit of Measures")
        model = UnitMeasure
        fields = ["um"]
        ordering = ["-id"]
