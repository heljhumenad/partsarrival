from django.db import models

from django.utils.translation import ugettext_lazy as _
from parts.core.models import TimeStampModel
from parts.models.managers.update_view import AbstractUpdateViewManager


class ServiceAdvisor(AbstractUpdateViewManager, TimeStampModel):

    DESIGNATION = [("SVC", "Service Advisor"), ("BRPSVC", "Service Advisor BRP")]

    first_name = models.CharField(
        max_length=200, verbose_name=_("First Name"), blank=False, unique=True
    )

    last_name = models.CharField(
        max_length=200, verbose_name=_("Last Name"), blank=False
    )

    designation = models.CharField(
        max_length=200, verbose_name=_("Designation"), choices=DESIGNATION
    )

    class Meta:
        db_table = _("service_advisor")
        verbose_name = _("Service Advisor")
        verbose_name_plural = _("Services Advisors")
        ordering = ["id"]

    def __str__(self):
        return "{0} {1}".format(self.first_name, self.last_name)
