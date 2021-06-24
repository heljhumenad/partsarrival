from django.db import models
from django.utils.translation import gettext_lazy as _


class UpdateViewManager(models.Manager):
    def get_object(self, query_pk_and_slug=True):
        return super().get_object().filter(id=self.kwargs["pk"]).first()

    def get_first_object(self, query_pk_and_slug=True):
        return super().get_first_object().filter(id=self.kwargs["pk"]).first()


class AbstractDescriptionModel(models.Model):

    description = models.CharField(
            max_length=200,
            verbose_name=_("Description")
    )

    class Meta:
        abstract = True


class AbstractUpdateViewManager(AbstractDescriptionModel, models.Model):
    objects = UpdateViewManager()

    class Meta:
        abstract = True
