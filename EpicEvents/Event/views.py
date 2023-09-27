from rest_framework import permissions, viewsets

from Event.models import Event
from Event.serializers import EventSerializer

from Event.permissions import EventPermission
from Client.permissions import CreateObjects, ReadOnly


class EventViewset(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [
        (permissions.IsAuthenticated & CreateObjects & EventPermission) or ReadOnly
    ]
