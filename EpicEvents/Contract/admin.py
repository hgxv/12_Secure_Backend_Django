from django.contrib import admin
from Contract.models import Contract


class ContractAdmin(admin.ModelAdmin):
    list_display = ("id", "client", "sales_contact", "status")


admin.site.register(Contract, ContractAdmin)
