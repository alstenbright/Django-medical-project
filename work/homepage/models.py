from django.db import models
from django.core.validators import MinLengthValidator

class Customer(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=10,validators=[MinLengthValidator(8)])
    