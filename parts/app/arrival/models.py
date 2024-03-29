from django.db import models
from django.utils.translation import gettext as _
from django.urls import reverse
from django.core.exceptions import ValidationError

from parts.app.advisor.models import ServiceAdvisor
from parts.app.partsnumber.models import (PartNumberClass, PartsNumber)
from parts.core.models import TimeStampModel
from parts.config.configurations import REMARKS
from parts.core.validators import (
    DEFAULT_QTY,
    DEFAULT_RO_RE_FORMAT
)


class PartsArrival(TimeStampModel):

    customer_name = models.CharField(
        verbose_name=_("Customer Name"),
        max_length=200
    )
    ro_number = models.CharField(
        verbose_name=_("RO/RE Number"),
        max_length=50, unique=True
    )
    item_class = models.ForeignKey(
        PartNumberClass,
        on_delete=models.CASCADE,
        verbose_name=_("Item Class")
    )
    advisor = models.ForeignKey(
        ServiceAdvisor,
        on_delete=models.CASCADE,
        verbose_name=_("Service Advisor")
    )
    partnumber = models.ForeignKey(
        PartsNumber,
        on_delete=models.CASCADE,
        verbose_name=_("Partsnumber")
    )
    qty = models.IntegerField(
        verbose_name=_("Quantity")
    )
    remarks = models.CharField(
        max_length=200,
        choices=REMARKS,
        verbose_name=_("Remarks")
    )
    reason = models.CharField(
        max_length=200,
        verbose_name=_("Reasons")
    )
    date_arrival = models.DateField(
        verbose_name=_("Date Arrival")
    )

    class Meta:
        db_table = _("arrival")
        verbose_name = _("Parts Arrival")
        verbose_name_plural = _("Parts Arrivals")
        ordering = ["id"]

    def __str__(self):
        return self.date_arrival

    def get_absolute_url(self):
        return reverse('arrival-read', args=[str(self.id)])

    @property
    def convert_date_string(self):
        from datetime import datetime

        # 9/5/2020 12:00 AM
        date_string = self.date_arrival
        return datetime.strptime(date_string, "%m/%d/%y %H:%M:%S")

    def clean(self):
        if self.qty > DEFAULT_QTY:
            raise ValidationError(
                    _("Error %(qty)s quantity"),
                    params={"qty": self.qty}
            )
        elif DEFAULT_RO_RE_FORMAT not in self.ro_number:
            raise ValidationError(
                _("Error %(ro_number)s not a valid format"),
                params = {"ro_number": self.ro_number}
            )
        return self
