from django.db import models
from django.db.models import Manager, QuerySet

class AppQuerySet(QuerySet):
    def delete(self):
        self.update(is_deleted=True)

class AppManager(Manager):
    def get_queryset(self):
        return AppQuerySet(self.model, using=self._db).exclude(is_deleted=True)

class DefaultModelsField(models.Model):
    class Meta:
        abstract = True
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)

    objects = AppManager()
