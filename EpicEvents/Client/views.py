from rest_framework import permissions, viewsets
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend

from Client.models import Client
from Client.serializers import ClientSerializer

from Client.permissions import (
    CreateObjects,
    ClientAndContractPermission,
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
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ("first_name", "email")

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
