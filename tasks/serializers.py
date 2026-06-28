from rest_framework import serializers

from accounts.utils import get_available_users

from .models import Task



class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = "__all__"



class TeacherTaskStatusSerializer(serializers.ModelSerializer):

    class Meta:
        model = Task
        fields = (
            "status",
        )



def validate_employee(self, employee):

    request_user = self.context["request"].user

    allowed_users = get_available_users(
        request_user
    )

    if employee not in allowed_users:
        raise serializers.ValidationError(
            "Siz ushbu foydalanuvchiga vazifa bera olmaysiz."
        )

    return employee