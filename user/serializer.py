from rest_framework import serializers
from .models import User
from django.contrib.auth.hashers import make_password


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "first_name",
            "last_name",
            "password",
            "created_at",
            "updated_at",
            "is_deleted",
        ]

    def create(self, validated_data):
        user = User(
            username=validated_data.get("username"),
            first_name=validated_data.get("first_name"),
            last_name=validated_data.get("last_name"),
            password=make_password(validated_data.get("password")),
        )

        user.save()
        return user

    def update(self, instance, validated_data):
        instance.username = validated_data.get("username")
        instance.first_name = validated_data.get("first_name")
        instance.last_name = validated_data.get("last_name")
        instance.password = make_password(validated_data.get("password"))
        instance.save()
        return instance


#TODO validate unique username