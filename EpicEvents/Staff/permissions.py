from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsManagement(BasePermission):
    def has_permission(self, request, view):
        role = request.user.group
        if role == "MA":
            return True
        return False
