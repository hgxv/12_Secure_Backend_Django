from rest_framework import permissions, viewsets, status
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend

from Staff.models import Staff
from Staff.serializers import StaffSerializer, CreateStaffSerializer

from Staff.permissions import IsManagement


class StaffViewset(viewsets.ModelViewSet):
    queryset = Staff.objects.all()
    serializer_class = StaffSerializer
    permission_classes = [permissions.IsAuthenticated & IsManagement]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ("group", "username")

    def create(self, request):
        serializer = CreateStaffSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
