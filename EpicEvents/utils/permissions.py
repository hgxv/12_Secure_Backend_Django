from rest_framework.permissions import BasePermission, SAFE_METHODS

from Contract.models import Contract


class ReadOnly(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True


class CreateObjects(BasePermission):
    def has_permission(self, request, view):
        role = request.user.group
        if (view.action == "create") & (role != "SA"):
            return False
        return True


class ClientAndContractPermission(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in ["PUT", "PATCH"]:
            if isinstance(obj, Contract):
                sales_contact = obj.client.sales_contact
            else:
                sales_contact = obj.sales_contact

            if (sales_contact == request.user) or (request.user.group == "MA"):
                return True
            return False


class IsManagement(BasePermission):
    def has_permission(self, request, view):
        role = request.user.group
        if role == "MA":
            return True
        return False

    def has_object_permission(self, request, view):
        role = request.user.group
        if role == "MA":
            return True
        return False


class EventPermission(BasePermission):
    def has_object_permission(self, request, view, event):
        if event.support_contact or event.contract.sales_contact == request.user:
            print("ok")
            return True
        print("non")
        return False


class CantDelete(BasePermission):
    def has_permission(self, request, view):
        if request.method == "DELETE":
            return False
        return True

    def has_object_permission(self, request, view, obj):
        if request.method == "DELETE":
            return False
        return True
