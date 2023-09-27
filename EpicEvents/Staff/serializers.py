from rest_framework.serializers import ModelSerializer
from django.contrib.auth.models import Group

from Staff.models import Staff


class StaffSerializer(ModelSerializer):
    class Meta:
        model = Staff
        exclude = [
            "password",
            "is_staff",
            "is_active",
            "is_superuser",
            "date_joined",
            "user_permissions",
            "groups",
        ]


class CreateStaffSerializer(ModelSerializer):
    class Meta:
        model = Staff
        fields = ["id", "first_name", "last_name", "email", "password", "group"]

    def check_username(self, username, NextId=1):
        if Staff.objects.filter(username=username + str(NextId)).exists():
            NextId += 1
            return self.check_username(username, NextId)

        else:
            username += str(NextId)
            return username

    def create(self, data):
        print("create", data)
        username = data["first_name"][0].casefold() + "." + data["last_name"].casefold()
        username = self.check_username(username)

        user = Staff.objects.create_user(username, data["email"], data["password"])

        user.first_name = data["first_name"]
        user.last_name = data["last_name"]

        for role in Staff.GROUP_CHOICE:
            if data["group"] in role:
                group_name = role[1]
                print(group_name)
                group = Group.objects.get(name=group_name)

                user.group = data["group"]
                user.groups.add(group)
                user.save()
                return user
