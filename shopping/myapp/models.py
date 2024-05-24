from django.db import models

class Product(models.Model):
   name = models.CharField(max_length=255)
   price = models.DecimalField(max_digits=8,decimal_places=2)
   category=models.CharField(max_length=255)
   created_at=models.DateTimeField(auto_now_add=True)
