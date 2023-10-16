from rest_framework import permissions, viewsets
from rest_framework.response import Response

from Staff.models import Staff
from Staff.serializers import StaffSerializer, CreateStaffSerializer

from utils.permissions import IsManagement, CantDelete


class StaffViewset(viewsets.ModelViewSet):
    queryset = Staff.objects.all()
    serializer_class = StaffSerializer
    permission_classes = [permissions.IsAuthenticated & IsManagement & CantDelete]

    def create(self, request):
        serializer = CreateStaffSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
