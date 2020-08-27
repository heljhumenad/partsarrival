from django.db import models


class UpdateViewManager(models.Manager):

    def get_object(self, query_pk_and_slug=True):
        return super().get_object().filter(id=self.kwargs["id"]).first()


class AbstractUpdateViewManager(models.Model):
    class Meta:
        abstract = True

    objects = UpdateViewManager()
