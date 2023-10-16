from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

from Staff.models import Staff
from Contract.models import Contract


class Event(models.Model):
    contract = models.ForeignKey(Contract, on_delete=models.RESTRICT, null=True)
    support_contact = models.ForeignKey(
        Staff, null=True, on_delete=models.RESTRICT, limit_choices_to={"group": "SU"}
    )
    date_created = models.DateTimeField(null=True)
    date_updated = models.DateTimeField(null=True)
    status = models.BooleanField(default=True)
    attendees = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(200)], null=True
    )
    event_start = models.DateTimeField(null=True)
    event_end = models.DateTimeField(null=True)
    location = models.CharField(max_length=250, null=True)
    notes = models.TextField(null=True)
