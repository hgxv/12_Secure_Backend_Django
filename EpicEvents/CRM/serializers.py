from rest_framework.serializers import ModelSerializer
from django.contrib.auth.models import Group
from CRM.models import Client, Contract, Event, Staff


class ClientSerializer(ModelSerializer):
    class Meta:
        model = Client
        fields = "__all__"


class ContractSerializer(ModelSerializer):
    class Meta:
        model = Contract
        fields = "__all__"

    def create(self, data):
        client = Client.objects.get(id=data["client"])
        if client.is_client == False:
            client.isclient = True


class EventSerializer(ModelSerializer):
    class Meta:
        model = Event
        fields = "__all__"


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

        group_name = Staff.GROUPS[data["group"]]
        group = Group.objects.get(name=group_name)

        user.group = data["group"]
        user.groups.add(group)

        user.save()
        return user
