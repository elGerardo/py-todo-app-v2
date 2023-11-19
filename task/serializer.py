from rest_framework import serializers
from .models import Task

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = [
            "id", 
            "user_id", 
            "title", 
            "description",
            "color", 
            "type", 
            "created_at",
            "updated_at",
            "is_deleted",
        ]

    def create(self, validated_data):
        task = Task(
            user_id=validated_data["user_id"],
            title=validated_data["title"],
            description=validated_data["description"],
            color=validated_data["color"],
            type=validated_data["type"],
        )

        task.save()
        return task