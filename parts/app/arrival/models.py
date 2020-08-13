from django.db import models
from django.utils.translation import ugettext_lazy as _

from parts.app.models.timestamp import TimeStampModel
from parts.app.partsnumber.models import PartNumberClass, PartsNumber
from parts.app.advisor.models import ServiceAdvisor


class PartsArrival(TimeStampModel):

    REMARKS = [
        ("COMPLETED", "COMPLETED"),
        ("NOT COMPLETED", "NOT COMPLETED"),
        ("LACKING", "LACKING"),
    ]

    class Meta:
        db_table = _("arrival")
        verbose_name = _("Parts Arrival")
        verbose_name_plural = _("Parts Arrivals")
        ordering = ["id"]

    customer_name = models.CharField(
        verbose_name=_("Customer Name"),
        max_length=200,
    )

    ro_number = models.CharField(
        verbose_name=_("RO/RE Number"),
        max_length=50
    )

    item_class = models.ForeignKey(
        PartNumberClass,
        on_delete=models.CASCADE,
        verbose_name=_("Item Class")
    )

    advisor = models.ForeignKey(
        ServiceAdvisor,
        on_delete=models.CASCADE,
        verbose_name=_("Service Advisor"),
    )

    partnumber = models.ForeignKey(
        PartsNumber,
        on_delete=models.CASCADE,
        verbose_name=_("Part Number"),
    )

    qty = models.IntegerField(
        verbose_name=_("Quantity"),
    )

    remarks = models.CharField(
        max_length=200,
        choices=REMARKS,
        verbose_name=_("Remarks"),
    )

    reason = models.CharField(
        max_length=200,
        verbose_name=_("Reasons")
    )

    date_arrival = models.CharField(
        verbose_name=_("Date Arrival"),
        max_length=20,
    )
