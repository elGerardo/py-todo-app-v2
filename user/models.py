import uuid
from django.db import models

# Create your models here.
class User(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    username = models.CharField(max_length=255, null=False, editable=True)
    first_name = models.CharField(max_length=255, null=False, editable=True)
    last_name = models.CharField(max_length=255, null=False, editable=True)
    email = models.CharField(max_length=255, null=False, editable=True)
    password = models.CharField(max_length=255, null=False, editable=True)

    class Meta:
        db_table = 'users'