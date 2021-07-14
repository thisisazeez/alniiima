from django.db import models

# Create your models here.

class user(models.Model):
    name = models.TextField(max_length=100)
