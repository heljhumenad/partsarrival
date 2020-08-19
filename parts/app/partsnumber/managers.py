from django.db import models 

class PartsNumberManager(models.Manager):
    
    def get_object(self, query_pk_and_slug=True):
        return super().get_object().filter(id=self.kwargs["id"]).first()