from rest_framework.serializers import ModelSerializer

from django.utils import timezone

from Event.models import Event


class EventSerializer(ModelSerializer):
    class Meta:
        model = Event
        fields = "__all__"

    def update(self, instance, validated_data):
        instance = super().update(instance, validated_data)
        if instance.status is False:
            instance.contract.status = "DO"
            instance.contract.save()
        instance.date_updated = timezone.now()
        instance.save()
        return instance
