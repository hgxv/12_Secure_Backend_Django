from django.contrib import admin
from Event.models import Event


class EventAdmin(admin.ModelAdmin):
    list_display = ("id", "contract", "support_contact", "status")


admin.site.register(Event, EventAdmin)
