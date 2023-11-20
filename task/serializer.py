from rest_framework import serializers
from .models import Task
from step.serializer import StepSerializer
from django.db import transaction

class TaskSerializer(serializers.ModelSerializer):
    def __init__(self, *args, **kwargs):
        self.step_fields = kwargs.pop('step_fields', None)
        super(TaskSerializer, self).__init__(*args, **kwargs)

    steps = StepSerializer(many=True, read_only=True)

    class Meta:
        model = Task
        fields = [
            "id", 
            "user", 
            "title", 
            "description",
            "color", 
            "type",
            "status", 
            "created_at",
            "updated_at",
            "is_deleted",
            "steps"
        ]

    def to_representation(self, instance):
        representation = super(TaskSerializer, self).to_representation(instance)
        representation['user_id'] = representation.pop('user')
        return representation

    def create(self, validated_data):
        with transaction.atomic():
            has_errors = "False"
            step_serializer_errors = []

            task = Task(
                user=validated_data["user"],
                title=validated_data["title"],
                description=validated_data["description"],
                color=validated_data["color"],
                type=validated_data["type"],
            )

            if 'status' in validated_data:
                task.status = validated_data["status"]

            task.save()

            if self.step_fields is not None:
                for step in self.step_fields:
                    body = {**step, "task":task.id}
                    step_serializer = StepSerializer(data=body)
                    if step_serializer.is_valid():
                        step_serializer.save()
                    else:
                        has_errors = "True"
                        step_serializer_errors.append(step_serializer.errors)
                        
            if has_errors == "True":
                transaction.set_rollback(True)
                return step_serializer_errors

            return task
    
#TODO validate the status
# NOT_STARTED, IN_PROGRESS, FINISHED

#TODO validate the color to hexa #FFFF01