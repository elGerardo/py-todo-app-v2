from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from .models import User

class UserSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(write_only=True)

    def validate(self, data):
        password = data.get('password')
        confirm_password = data.get('confirm_password')

        if password != confirm_password:
            raise serializers.ValidationError({"confirm_password": ["confirm_password is not the same"]})

        return data

    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "password",
            "created_at",
            "updated_at",
            "is_deleted",
            "confirm_password",  # Agregar el campo confirm_password al serializer
        ]

    def create(self, validated_data: dict) -> User:
        user = User(
            username=validated_data.get("username"),
            password=make_password(validated_data.get("password")),
        )

        user.save()
        return user

    def update(self, instance: User, validated_data: dict) -> User:
        instance.username = validated_data.get("username")
        instance.password = make_password(validated_data.get("password"))
        instance.save()
        return instance
