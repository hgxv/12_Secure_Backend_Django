from rest_framework.permissions import BasePermission, SAFE_METHODS
from CRM.models import *


class ReadOnly(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True


class IsManagement(BasePermission):
    def has_permission(self, request, view):
        role = request.user.group
        if role == "MA":
            return True
        return False


class CreateObjects(BasePermission):
    def has_permission(self, request, view):
        role = request.user.group
        if (view.action == "create") & (role != "SA"):
            return False
        return True


class ClientAndContractPermission(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in ["PUT", "DELETE"]:
            if isinstance(obj, Contract):
                sales_contact = obj.client.sales_contact
            else:
                sales_contact = obj.sales_contact

            if sales_contact != request.user:
                return False
            return True


class EventPermission(BasePermission):
    def has_object_permission(self, request, view, client):
        if client.support_contact == request.user:
            return True
        return False
