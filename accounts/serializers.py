from rest_framework import serializers
from .models import User



class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True,
        min_length=8
    )

    class Meta:
        model = User
        fields = (
            "login",
            "full_name",
            "phone",
            "email",
            "position",
            "salary",
            "hire_date",
            "password",
        )

    def create(self, validated_data):
        password = validated_data.pop("password")

        user = User(**validated_data)
        user.set_password(password)
        user.save()

        return user





from rest_framework_simplejwt.serializers import (
    TokenObtainPairSerializer
)
from django.utils import timezone


class LoginSerializer(TokenObtainPairSerializer):

    @classmethod
    def get_token(cls, user):
        return super().get_token(user)

    def validate(self, attrs):
        data = super().validate(attrs)

        user = self.user

        return {
            "message": "Login muvaffaqiyatli amalga oshirildi",

            "user": {
                "id": user.id,
                "login": user.login,
                "role": user.position,
            },

            "tokens": {
                "access": data["access"],
                "refresh": data["refresh"],
            },

            "faculty": user.faculty.name if user.faculty else None,
            "department": user.department.name if user.department else None,
            "is_active": user.is_active,
            "is_staff": user.is_staff,
            "is_superuser": user.is_superuser,

            "login_at": timezone.now(),
        }