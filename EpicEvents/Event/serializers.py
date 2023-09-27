from rest_framework.serializers import ModelSerializer
from Contract.models import Contract

from django.utils import timezone

from Event.models import Event


class EventSerializer(ModelSerializer):
    class Meta:
        model = Event
        fields = "__all__"

    def create(self, data):
        contract = Contract.objects.get(id=data["contract"])
        if contract.status == "NC":
            contract.status = "OG"
        return contract

    def update(self, instance, validated_data):
        instance = super().update(instance, validated_data)
        instance.date_updated = timezone.now()
        return instance
