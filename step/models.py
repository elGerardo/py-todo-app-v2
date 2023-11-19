import uuid
from django.db import models
from task.models import Task
from todoapp.helpers.default_models_field import DefaultModelsField

# Create your models here.    
class Step(DefaultModelsField):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    task_id = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='task_id')
    title = models.CharField(max_length=255, null=False, editable=True)
    description = models.CharField(max_length=255, null=False, editable=True)
    color = models.CharField(max_length=255, null=False, editable=True)
    order = models.IntegerField(null=False, editable=True)

    class Meta:
        db_table = 'steps'
    

