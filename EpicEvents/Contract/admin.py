from django.contrib import admin
from Contract.models import Contract


class ContractAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "client",
        "sales_contact",
        "date_created",
        "date_updated",
        "amount",
        "payment_due",
        "status",
    )


admin.site.register(Contract, ContractAdmin)
