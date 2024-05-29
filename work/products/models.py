from django.db import models


class Product(models.Model):
    medical_name = models.CharField(max_length=500)
    description = models.TextField()
    medical_price = models.DecimalField(max_digits=10, decimal_places=2)
    
    