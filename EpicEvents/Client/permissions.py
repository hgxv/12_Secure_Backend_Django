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
            print("ici")
            return False
        return True


class ClientAndContractPermission(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in ["PUT", "PATCH", "DELETE"]:
            if isinstance(obj, Contract):
                sales_contact = obj.client.sales_contact
            else:
                sales_contact = obj.sales_contact

            if sales_contact != request.user:
                print(sales_contact)
                return False
            return True
