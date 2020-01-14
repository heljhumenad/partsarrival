from django.db import models
from django.utils.translation import gettext_lazy as _

from parts.app.models.timestamp import TimeStampModel

class PartsNumber(TimeStampModel):

    partnumber = models.CharField(max_length=200,
                                  verbose_name = _("Parts Number"),
                                  )

    unit_measure = models.ForeignKey('UnitMeasure',
                                     verbose_name=_("Unit of Measure"),
                                     on_delete=models.CASCADE,)

    description = models.CharField(max_length=200,
                                   verbose_name=_("Part Number Description"),
                                  )
    

class UnitMeasure(TimeStampModel):

     um = models.CharField(max_length=20,
                           verbose_name=_("Unit of Measure")
                          )
