from rest_framework import permissions, viewsets
from rest_framework.response import Response

from Event.models import Event
from Contract.models import Contract

from Event.serializers import EventSerializer

from utils.permissions import CreateObjects, ReadOnly, EventPermission, CantDelete

from django.utils import timezone


class EventViewset(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [
        (permissions.IsAuthenticated & CreateObjects & EventPermission & CantDelete)
        or ReadOnly
    ]

    def create(self, request, contracts_pk):
        serializer = self.serializer_class(
            data=request.data, context={"request": request}
        )
        contract = Contract.objects.get(pk=contracts_pk)
        if Event.objects.filter(contract=contracts_pk).exists():
            return Response("An event already exists for this contract.")

        contract.status = "OG"
        contract.save()

        if serializer.is_valid():
            serializer.save(contract=contract, date_created=timezone.now())
            return Response(serializer.data)

        else:
            return Response(serializer.errors)
