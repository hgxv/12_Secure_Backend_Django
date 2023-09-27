from rest_framework.serializers import ModelSerializer
from Client.models import Client

from django.utils import timezone


class ClientSerializer(ModelSerializer):
    class Meta:
        model = Client
        fields = "__all__"

    def update(self, instance, validated_data):
        instance = super().update(instance, validated_data)
        instance.date_updated = timezone.now()
        return instance
