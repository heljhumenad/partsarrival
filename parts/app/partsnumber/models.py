from django.db import models
from django.utils.translation import gettext_lazy as _
from django.urls import reverse
from django.core.exceptions import ValidationError

from parts.core.managers import AbstractUpdateViewManager
from parts.core.models import TimeStampModel
from parts.core.validators import MAX_VALUE_OF_PARTNUMBER
from parts.config.configurations import PARTNUMBER_STATUS


class PartsNumber(AbstractUpdateViewManager, TimeStampModel):

    # Partnumber will be indicator for the receiving end that this
    # item was from the manufacturer that been delivered to the selling company
    # all part number will be standardize in this context
    # each company vary different approach of naming of its partnumber mostly 
    # they will proceed the naming from its manufacturer partnumber

    partnumber = models.CharField(
        max_length=200,
        verbose_name=_("Parts Number")
    )
    source_code = models.ForeignKey(
        "SourceCode",
        verbose_name=_("Source Code"),
        on_delete = models.CASCADE
    )
    bar_code = models.CharField(
        max_length=200,
        verbose_name=_("Barcode No.")
    )

    selling_price = models.IntegerField(
        verbose_name=_("Selling Price")
    )

    status = models.CharField(
        max_length=200,
        verbose_name=_("Status"),
        choices=PARTNUMBER_STATUS
    )
    unit_measure = models.ForeignKey(
        "UnitMeasure",
        verbose_name=_("Stock/UM"),
        on_delete=models.CASCADE
    )

    class Meta:
        db_table = _("partnumbers")
        verbose_name = _("Part Number")
        verbose_name_plural = _("Parts Number")
        ordering = ["id"]

    def __str__(self):
        return self.partnumber

    def get_absolute_url(self):
        return reverse('parts_number_read_view', args=[str(self.id)])

    # !Find way to handle this feat in template
    @property
    def add_leading_zero(self):
        return str(self.selling_price) + ".00"

    def clean(self):
        if (len(self.partnumber) != MAX_VALUE_OF_PARTNUMBER or 
            len(self.partnumber) > MAX_VALUE_OF_PARTNUMBER):
                raise ValidationError(
                        _("Partsnumber %(partnumber)s size is not valid"),
                        params = {"partnumber": self.partnumber},
                )
        return self


class UnitMeasure(AbstractUpdateViewManager, TimeStampModel):

    # SKU - unit of the parts
    # handles the unit of measure of the parts number
    # ex. kg, sm, lg, tons or pcs
    
    # SKU - unit of measure
    sku_um = models.CharField(
        max_length=20,
        verbose_name=_("Unit of Measure")
    )

    class Meta:
        db_table = _("um")
        verbose_name = _("Unit of Measure")
        verbose_name_plural = _("Unit of Measures")
        ordering = ["id"]

    def __str__(self):
        return self.um


class PartNumberClass(AbstractUpdateViewManager, TimeStampModel):

    # Handles the class the part number belong
    # ex cords, wires, tire, or other types class the part number belongs

    class_name = models.CharField(
        max_length=20,
        verbose_name=_("Class name")
    )

    charge_type = models.CharField(
        max_length=20,
        verbose_name=_("Charge Type")
    )

    class Meta:
        db_table = _("partnumber_class")
        verbose_name = _("Part Number Class")
        verbose_name_plural = _("Part Number Classes")
        ordering = ["id"]

    def __str__(self):
        return self.class_name.upper()

    def get_absolute_url(self):
        return reverse('item_class_read', args=[str(self.id)])


class SourceCode(AbstractUpdateViewManager, TimeStampModel):

    # Source code - number description of its authenticity 
    # mostly it determine that the partnumber is authentic or a syntetically made from the manufacturing
    

    # it will tell programtically base on the source code of the parts 
    # it will put on the end of the partsnumber (ex. 122304-19023-01) 
    # where `01` will be the indicator of its authenticity
    # the company will be customizing this base on the need of its own company to determine other factors
    # of segrations of parts that is authentic and syntetically made

    code = models.CharField(
        max_length=20,
        verbose_name= _("Number Code"),
    )

    desc = models.CharField(
        max_length=200,
        verbose_name=_("Soure Code Description"),
    )

    class Meta:
        db_table = _("source_code")
        verbose_name = _("Source Code")
        verbose_name_plural = _("Source Codes")
        ordering = ["id"]

    def __str__(self):
        return self.code

    def get_absolute_url(self):
        pass # TODO: create index.html file for source code


class SellingPrice(TimeStampModel):

    # All parts will be handle on different scheme of selling price 
    # it also handle discounts and base price for the product

    # TODO: check another field that will be use for selling prices
    selling_price = models.IntegerField(
            verbose_name = _("Selling Price")
    )

    discount_percentage = models.DecimalField(
            max_digits= 5,
            decimal_places = 2,
    )

    class Meta:
        db_table = _("selling_price")
        verbose_name = _("Selling Price")
        verbose_name_plural = _("Selling Prices")
        ordering = ["id"]

