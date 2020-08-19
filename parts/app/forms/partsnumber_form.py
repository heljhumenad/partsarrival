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

        def get_meta_fields_label(self):
            '''
            # Get all meta fields and verbose name in a object model
            # iterate through the fields the render in response template
            # each iteration will be used in table header
            # and each value of the iterated value will be the
            # output of the table
            '''
            pass

        def check_partnumber_unique(self, *args, **kwargs):
            '''
            Check the partnumber if its unique in value
            '''
            pass


class UnitofMeasureForm(forms.ModelForm):
    class Meta:
        verbose_name = _("Unit of Measure")
        verbose_name_plural = _("Unit of Measures")
        model = UnitMeasure
        fields = ["um"]
        ordering = ["-id"]
