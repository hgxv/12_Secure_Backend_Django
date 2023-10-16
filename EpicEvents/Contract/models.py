from django.db import models

from Client.models import Client
from Staff.models import Staff


class Contract(models.Model):
    client = models.ForeignKey(Client, on_delete=models.RESTRICT)
    sales_contact = models.ForeignKey(Staff, null=True, on_delete=models.RESTRICT)
    date_created = models.DateTimeField(null=True)
    date_updated = models.DateTimeField(null=True)
    STATUS_CHOICE = [("NC", "Not created"), ("OG", "On going"), ("DO", "Done")]
    status = models.CharField(
        default="NC", max_length=2, choices=STATUS_CHOICE, null=True
    )
    amount = models.FloatField(null=True)
    payment_due = models.DateTimeField(null=True)
