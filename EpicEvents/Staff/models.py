from django.db import models
from django.contrib.auth.models import AbstractUser


class Staff(AbstractUser):
    GROUP_CHOICE = [("SA", "Sales"), ("SU", "Support"), ("MA", "Management")]

    username = models.CharField(null=True, unique=True)
    email = models.EmailField(unique=True)
    group = models.CharField(max_length=2, choices=GROUP_CHOICE)
    REQUIRED_FIELDS = []
