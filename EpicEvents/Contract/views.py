from rest_framework import permissions, viewsets
from django_filters.rest_framework import DjangoFilterBackend

from Contract.models import Contract
from Contract.serializers import ContractSerializer

from utils.permissions import (
    CreateObjects,
    ClientAndContractPermission,
    ReadOnly,
    CantDelete,
)


class ContractViewset(viewsets.ModelViewSet):
    queryset = Contract.objects.all()
    serializer_class = ContractSerializer
    permission_classes = [
        (
            permissions.IsAuthenticated
            & CreateObjects
            & ClientAndContractPermission
            & CantDelete
        )
        or ReadOnly
    ]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ("client", "sales_contact", "status")
