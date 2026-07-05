from rest_framework.permissions import BasePermission

from accounts.models import (
    ROLE_ADMIN,
    ROLE_RECTOR,
    ROLE_VICE_RECTOR,
)


class IsAdminOrRektorOrViceRektor(BasePermission):

    message = "Sizda fakultet yaratish huquqi mavjud emas."

    def has_permission(self, request, view):
        user = request.user
        if not user.is_authenticated:
            return False
        
        if user.position in [ROLE_ADMIN, ROLE_RECTOR, ROLE_VICE_RECTOR]:
            return True
        return False
