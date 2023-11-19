import uuid
from django.db import models
from todoapp.helpers.default_models_field import DefaultModelsField
from user.models import User

# Create your models here.
class Task(DefaultModelsField):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_id')
    title = models.CharField(max_length=255, null=False, editable=True)
    description = models.CharField(max_length=255, null=False, editable=True)
    color = models.CharField(max_length=255, null=False, editable=True)
    type = models.CharField(max_length=255, null=False, editable=True)

    class Meta:
        db_table = 'tasks'