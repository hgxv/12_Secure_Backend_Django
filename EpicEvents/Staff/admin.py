from django.contrib import admin
from django.contrib.auth.admin import GroupAdmin, UserAdmin
from django.contrib.auth.models import Group
from Staff.models import Staff


class CustomUserAdmin(UserAdmin):
    list_display = ("username", "id", "first_name", "last_name", "group", "email")


admin.site.unregister(Group)


class UserInLine(admin.TabularInline):
    model = Group.user_set.through
    extra = 0


@admin.register(Group)
class GenericGroup(GroupAdmin):
    inlines = [UserInLine]


admin.site.register(Staff, CustomUserAdmin)
