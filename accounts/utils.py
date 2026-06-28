from accounts.models import (
    User,
    ROLE_RECTOR,
    ROLE_VICE_RECTOR,
    ROLE_DEAN,
    ROLE_HEAD_OF_DEPARTMENT,
    ROLE_TEACHER,
)



def get_available_users(user):

    if user.position == ROLE_RECTOR:
        return User.objects.filter(
            position__in=[
                ROLE_VICE_RECTOR,
                ROLE_DEAN,
                ROLE_HEAD_OF_DEPARTMENT,
                ROLE_TEACHER,
            ]
        )

    elif user.position == ROLE_VICE_RECTOR:
        return User.objects.filter(
            position__in=[
                ROLE_DEAN,
                ROLE_HEAD_OF_DEPARTMENT,
                ROLE_TEACHER,
            ]
        )

    elif user.position == ROLE_DEAN:
        return User.objects.filter(
            faculty=user.faculty,
            position__in=[
                ROLE_HEAD_OF_DEPARTMENT,
                ROLE_TEACHER,
            ]
        )

    elif user.position == ROLE_HEAD_OF_DEPARTMENT:
        return User.objects.filter(
            department=user.department,
            position=ROLE_TEACHER
        )

    return User.objects.none()