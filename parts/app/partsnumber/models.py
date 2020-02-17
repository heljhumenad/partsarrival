from django.db import models
from django.utils.translation import gettext_lazy as _

from parts.app.models.timestamp import TimeStampModel


class PartsNumber(TimeStampModel):

    partnumber = models.CharField(max_length=200,
                                  verbose_name=_("Parts Number"),
                                  )

    unit_measure = models.ForeignKey('UnitMeasure',
                                     verbose_name=_("Unit of Measure"),
                                     on_delete=models.CASCADE,)

    description = models.CharField(max_length=200,
                                   verbose_name=_("Description"),
                                   )

    class Meta:
        db_table = _('partnumbers')
        verbose_name = _("Part Number")
        verbose_name_plural = _("Parts Number")
        ordering = ['id']

    def __str__(self):
        return self.partnumber


class UnitMeasure(TimeStampModel):

    um = models.CharField(max_length=20,
                          verbose_name=_("Unit of Measure")
                          )

    class Meta:
        db_table = _("um")
        verbose_name = _("Unit of Measure")
        verbose_name_plural = _("Unit of Measures")
        ordering = ['id']

    def __str__(self):
        return self.um
