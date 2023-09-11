from rest_framework import permissions, viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from CRM.models import Client, Contract, Event, Staff
from CRM.serializers import (
    ClientSerializer,
    ContractSerializer,
    EventSerializer,
    StaffSerializer,
    CreateStaffSerializer,
)
from CRM.permissions import (
    IsManagement,
    CreateObjects,
    ClientAndContractPermission,
    EventPermission,
    ReadOnly,
)

from django.utils import timezone


class ClientViewset(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    permission_classes = [
        permissions.IsAuthenticated & CreateObjects & ClientAndContractPermission
        or ReadOnly
    ]

    def list(self, request):
        queryset = self.queryset
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        try:
            client = Client.objects.get(pk=pk)
            serializer = self.serializer_class(client)
            return Response(serializer.data)

        except Client.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def create(self, request):
        serializer = self.serializer_class(
            data=request.data, context={"request": request}
        )
        if serializer.is_valid():
            serializer.save(date_created=timezone.now(), sales_contact=request.user)
            return Response(serializer.data)

        else:
            print(serializer.data)
            return Response("Something went wrong with provided data.")

    def update(self, request, pk=None):
        try:
            client = Client.objects.get(pk=pk)
            self.check_object_permissions(request, client)
            serializer = self.serializer_class(
                instance=client, data=request.data, partial=True
            )

            if serializer.is_valid():
                self.perform_update(serializer)
                return Response(serializer.data)

            else:
                return Response(serializer.errors)

        except Client.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)


class ContractViewset(viewsets.ModelViewSet):
    queryset = Contract.objects.all()
    serializer_class = ContractSerializer
    permission_classes = [
        permissions.IsAuthenticated
        & CreateObjects
        & ReadOnly
        & ClientAndContractPermission
    ]

    def list(self, request):
        serializer = self.serializer_class(self.queryset)
        return Response(serializer.data)


class EventViewset(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [
        permissions.IsAuthenticated & CreateObjects & ReadOnly & EventPermission
    ]

    def list(self, request):
        serializer = self.serializer_class(self.queryset)
        return Response(serializer.data)


class StaffViewset(viewsets.ModelViewSet):
    queryset = Staff.objects.all()
    serializer_class = StaffSerializer
    permission_classes = [permissions.IsAuthenticated & IsManagement]

    def list(self, request):
        serializer = self.serializer_class(self.queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = CreateStaffSerializer(
            data=request.data, context={"request": request}
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        else:
            print("wrong", serializer.data)
            return Response("Something went wrong with provided data.")
