from django.db import models
from django.utils.translation import ugettext_lazy as _

from parts.app.models.timestamp import TimeStampModel
from parts.app.partsnumber.models import PartNumberClass, PartsNumber
from parts.app.advisor.models import ServiceAdvisor

"""
# Model field

customer name - CharField 
ro number - Charfield
class - foreign key item_class
advisor - foreign key service advisor
partnumber - foreign key partnumber
description - description partnumber
qty - Charfield qty
remarks = [completed, not complete, lacking,] - choices
date arrival - date and time
date inputed - auto now
"""


class PartsArrival(TimeStampModel):

    REMARKS = [
        ("COMPLETED", "COMPLETED"),
        ("NOT COMPLETE", "NOT COMPLETE"),
        ("LACKING", "LACKING"),
    ]

    class Meta:
        db_table = _("arrival")
        verbose_name = _("Parts Arrival")
        versbose_name_plural = _("Parts Arrivals")
        ordering = ["id"]

    customer_name = models.CharField(
        verbose_name=_("Customer Name"),
        max_length=200,
    )

    ro_number = models.CharField(
        verbose_name=_("Ro Number"),
        max_length=50
    )

    item_class = models.ForeignKey(
        "PartNumberClass", 
        on_delete=models.CASCADE,
        verbose_name=_("Item Class")
    )

    advisor = models.ForeignKey(
        "ServiceAdvisor",
        on_delete=models.CASCADE,
        verbose_name=_("Service Advisor"),
    )

    partnumber = models.ForeignKey(
        "PartNumber",
        on_delete=models.CASCADE,
        verbose_name=_("Part Number"),
    )

    description = models.CharField(
        max_length=200,
        verbose_name=_("Description"),
    )

    qty = models.IntegerField(
        max_length=200,
        verbose_name=_("Quantity"),
    )

    remarks = models.CharField(
        max_length=200,
        choices=REMARKS,
        verbose_name=_("Remarks"),
    )

    date_arrival = models.DateTimeField(
        verbose_name=_("Date Arrival"),
    )
