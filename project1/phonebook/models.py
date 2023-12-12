from django.db import models

# Create your models here.

class PhoneNumber(models.Model):
    creator = models.TextField(unique=True)
    name = models.TextField()
    number = models.TextField()