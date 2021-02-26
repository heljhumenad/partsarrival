from django.db import models
from django.utils.translation import gettext_lazy as _

class UpdateViewManager(models.Manager):

    def get_object(self, query_pk_and_slug=True):
        return super().get_object().filter(id=self.kwargs["pk"]).first()

    def get_first_object(self):
        return super().get_first_object().filter(id=self.kwargs["pk"]).first()


class AbstractUpdateViewManager(models.Model):
    class Meta:
        abstract = True

    objects = UpdateViewManager()

    description = models.CharField(
        max_length=200,
        verbose_name = _("Description")
    )
