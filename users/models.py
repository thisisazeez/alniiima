from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUsers(AbstractUser):
    age = models.PositiveIntegerField(null=True, blank=True)
    phone_number =models.IntegerField(null=True, blank=True)
