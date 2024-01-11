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
    
    def create(self, validated_data: dict) -> Step:
        step = Step(
            task = validated_data.get('task'),
            title = validated_data.get('title'),
            color = validated_data.get('color'),
            order = validated_data.get('order')
        )

        if 'description' in validated_data:
            step.description = validated_data.get('description')

        if 'status' in validated_data:
            step.status = validated_data.get('status')

        step.save()
        return step
    
    def update(self, instance: Step, validated_data: dict) -> Step:
        instance.task = validated_data.get("task")
        instance.title = validated_data.get("title")
        instance.color = validated_data.get("color")
        instance.order = validated_data.get("order")

        if 'status' in validated_data:
            instance.status = validated_data.get("status")

        if 'description' in validated_data:  
            instance.description = validated_data.get("description")
        
        instance.save()
        return instance
