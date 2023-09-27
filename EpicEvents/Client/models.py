from django.db import models

from Staff.models import Staff


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
