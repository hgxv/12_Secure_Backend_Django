from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MaxValueValidator, MinValueValidator


class Staff(AbstractUser):
    GROUP_CHOICE = [("SA", "SALES"), ("SU", "SUPPORT"), ("MA", "MANAGEMENT")]

    username = models.CharField(null=True, unique=True)
    email = models.EmailField(unique=True)
    group = models.CharField(max_length=2, choices=GROUP_CHOICE)
    REQUIRED_FIELDS = []


class Client(models.Model):
    first_name = models.CharField(max_length=25, null=True)
    last_name = models.CharField(max_length=25, null=True)
    email = models.CharField(max_length=100, null=True)
    phone = models.CharField(max_length=20, null=True)
    mobile = models.CharField(max_length=20, null=True)
    company_name = models.CharField(max_length=250, null=True)
    date_created = models.DateTimeField(null=True)
    date_updated = models.DateTimeField(null=True)
    sales_contact = models.ForeignKey(Staff, null=True, on_delete=models.SET_NULL)
    is_client = models.BooleanField(default=False)


class Contract(models.Model):
    client = models.ForeignKey(Client, null=True, on_delete=models.SET_NULL)
    sales_contact = models.ForeignKey(Staff, null=True, on_delete=models.SET_NULL)
    date_created = models.DateTimeField(null=True)
    date_updated = models.DateTimeField(null=True)
    status = models.BooleanField(default=False, null=True)
    amount = models.FloatField(null=True)
    payment_due = models.TimeField(null=True)


class Event(models.Model):
    contract = models.ForeignKey(Contract, on_delete=models.CASCADE)
    support_contact = models.ForeignKey(Staff, null=True, on_delete=models.SET_NULL)
    date_created = models.DateTimeField(null=True)
    date_updated = models.DateTimeField(null=True)
    status = models.BooleanField(default=True, null=True)
    attendees = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(200)], null=True
    )
    event_start = models.DateTimeField(null=True)
    event_end = models.DateTimeField(null=True)
    location = models.CharField(max_length=250, null=True)
    notes = models.TextField(null=True)
