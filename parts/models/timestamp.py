from django.db import models
from django.utils.translation import gettext_lazy as _


class TimeStampModel(models.Model):
    class Meta:
        abstract = True

    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_("Created At"),
    )

    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name=_("Updated At"),
    )
