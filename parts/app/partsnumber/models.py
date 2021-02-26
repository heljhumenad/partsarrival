from django.db import models
from django.utils.translation import gettext_lazy as _

from parts.models.timestamp import TimeStampModel
from parts.models.managers.update_view import AbstractUpdateViewManager


class PartsNumber(AbstractUpdateViewManager, TimeStampModel):

    SOURCE_CODE = [
        ("01", "Nissan Japan"),
        ("02", "Nissan Taiwan"),
        ("05", "Nissan Thailand"),
        ("08", "Nissan Indonesia"),
    ]

    PARTNUMBER_STATUS = [
        ("Active", "Active"),
        ("Depcreated", "Depcreated"),
        ("Obsolete", "Obsolete"),
        ("Deactivated", "Deactivated"),
    ]

    partnumber = models.CharField(max_length=200, verbose_name=_("Parts Number"), unique=True)

    source_code = models.CharField(
        max_length=200, verbose_name=_("Parts Number"), choices=SOURCE_CODE
    )

    bar_code = models.CharField(max_length=200, verbose_name=_("Barcode No."))

    selling_price = models.IntegerField(verbose_name=_("Selling Price"))

    status = models.CharField(max_length=200, verbose_name=_("Status"), choices=PARTNUMBER_STATUS)

    unit_measure = models.ForeignKey(
        "UnitMeasure",
        verbose_name=_("Stock/UM"),
        on_delete=models.CASCADE,
    )

    class Meta:
        db_table = _("partnumbers")
        verbose_name = _("Part Number")
        verbose_name_plural = _("Parts Number")
        ordering = ["id"]

    def __str__(self):
        return self.partnumber


class UnitMeasure(AbstractUpdateViewManager, TimeStampModel):

    um = models.CharField(
        max_length=20,
        verbose_name=_("Unit of Measure"),
    )

    class Meta:
        db_table = _("um")
        verbose_name = _("Unit of Measure")
        verbose_name_plural = _("Unit of Measures")
        ordering = ["id"]

    def __str__(self):
        return self.um


class PartNumberClass(AbstractUpdateViewManager, TimeStampModel):

    class_name = models.CharField(max_length=20, verbose_name=_("Class name"))

    # Add charge type using class name insert
    charge_type = models.CharField(
        max_length=20,
        verbose_name=_("Charge Type"),
    )

    class Meta:
        db_table = _("partnumber_class")
        verbose_name = _("Part Number Class")
        verbose_name_plural = _("Part Number Classes")
        ordering = ["id"]

    def __str__(self):
        return self.class_name.upper()
