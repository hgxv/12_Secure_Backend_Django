from django.contrib import admin
from django.contrib.auth.admin import GroupAdmin
from django.contrib.auth.models import Group
from CRM.models import Client, Contract, Event, Staff


class StaffAdmin(admin.ModelAdmin):
    list_display = ("username", "id", "group", "email")


class ClientAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "first_name",
        "last_name",
        "company_name",
        "sales_contact",
        "is_client",
    )


class ContractAdmin(admin.ModelAdmin):
    list_display = ("id", "client", "sales_contact", "status")


class EventAdmin(admin.ModelAdmin):
    list_display = ("id", "contract", "support_contact", "status")


admin.site.unregister(Group)


class UserInLine(admin.TabularInline):
    model = Group.user_set.through
    extra = 0


@admin.register(Group)
class GenericGroup(GroupAdmin):
    inlines = [UserInLine]


admin.site.register(Staff, StaffAdmin)
admin.site.register(Client, ClientAdmin)
admin.site.register(Contract, ContractAdmin)
admin.site.register(Event, EventAdmin)
