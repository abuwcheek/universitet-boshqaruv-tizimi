from .models import Task
from accounts.models import (
    ROLE_RECTOR,
    ROLE_VICE_RECTOR,
    ROLE_DEAN,
    ROLE_HEAD_OF_DEPARTMENT,
    ROLE_TEACHER,
)



def get_task_queryset(user):

    if user.position == ROLE_RECTOR:
        return Task.objects.all()

    if user.position == ROLE_VICE_RECTOR:
        return Task.objects.filter(
            created_by=user
        ) | Task.objects.filter(
            employee__position__in=[
                ROLE_DEAN,
                ROLE_HEAD_OF_DEPARTMENT,
                ROLE_TEACHER,
            ]
        )

    if user.position == ROLE_DEAN:
        return Task.objects.filter(
            faculty=user.faculty
        )

    if user.position == ROLE_HEAD_OF_DEPARTMENT:
        return Task.objects.filter(
            department=user.department
        )

    if user.position == ROLE_TEACHER:
        return Task.objects.filter(
            employee=user
        )

    return Task.objects.none()