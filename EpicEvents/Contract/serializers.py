from rest_framework.serializers import ModelSerializer
from Contract.models import Contract

from django.utils import timezone


class ContractSerializer(ModelSerializer):
    class Meta:
        model = Contract
        fields = "__all__"

    def create(self, validated_data):
        contract = super().create(validated_data)
        contract.sales_contact = self.context["request"].user
        contract.date_created = timezone.now()
        contract.status = "NC"
        contract.save()
        return contract

    def update(self, instance, validated_data):
        instance = super().update(instance, validated_data)
        instance.date_updated = timezone.now()
        return instance
