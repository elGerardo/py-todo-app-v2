from rest_framework import serializers
from .models import Step

class StepSerializer(serializers.ModelSerializer):
    class Meta:
        model = Step
        fields = [
            "id",
            "task",
            "title",
            "description",
            "color",
            "order",
            "status",
            "created_at",
            "updated_at",
            "is_deleted",
        ]
        
    def to_representation(self, instance):
        representation = super(StepSerializer, self).to_representation(instance)
        representation['task_id'] = representation.pop('task')
        return representation
    
    def create(self, validated_data):
        step = Step(
            task = validated_data.get('task'),
            title = validated_data.get('title'),
            description = validated_data.get('description'),
            color = validated_data.get('color'),
            order = validated_data.get('order')
        )

        step.save()
        return step