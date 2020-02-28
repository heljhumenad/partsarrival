from django.db import models
from django.utils.translation import ugettext_lazy as _
from parts.app.models.timestamp import TimeStampModel

class ServiceAdvisor(TimeStampModel):

    DESIGNATION = [
        ('SVC', 'Service Advisor'),
        ('BRPSVC', 'Service Advisor BRP')
    ]

    first_name = models.CharField(
        max_length=200,
        verbose_name=_("First Name"),
        blank=False
    )

    last_name = models.CharField(
        max_length=200,
        verbose_name=_("Last Name"),
        blank = False
    )

    designation = models.CharField(
        max_length=200,
        verbose_name=_("Designation"),
        choices=DESIGNATION
    )

    class Meta:
        db_table = _("service_advisor")
        verbose_name = _("Service Advisor")
        verbose_name_plural = _("Services Advisors")
        ordering = ['id']

    def __str__(self):
        return "{0}, {1}" % (self.firstname, self.last_name)
    

