from django.contrib import admin
from Client.models import Client


class ClientAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "first_name",
        "last_name",
        "company_name",
        "sales_contact",
    )


admin.site.register(Client, ClientAdmin)
