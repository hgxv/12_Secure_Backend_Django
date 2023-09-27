from rest_framework.permissions import BasePermission, SAFE_METHODS


class EventPermission(BasePermission):
    def has_object_permission(self, request, view, event):
        if event.support_contact or event.contract.sales_contact == request.user:
            return True
        return False
