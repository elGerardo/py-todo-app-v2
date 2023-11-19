import uuid
from django.db import models
from todoapp.helpers.default_models_field import DefaultModelsField


# Create your models here.
class User(DefaultModelsField):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    username = models.CharField(unique=True, max_length=255, null=False, editable=True)
    first_name = models.CharField(max_length=255, null=False, editable=True)
    last_name = models.CharField(max_length=255, null=False, editable=True)
    is_active = models.BooleanField(default=True, editable=True)
    is_authenticated = models.BooleanField(default=False, editable=True)
    password = models.CharField(max_length=255, null=False, editable=True)

    REQUIRED_FIELDS = []
    USERNAME_FIELD = 'username'
    is_anonymous = False
    
    def __str__(self):
        return self.username

    class Meta:
        db_table = "users"
