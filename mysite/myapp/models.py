from django.db import models

class Profile(models.Model):
    name=models.CharField(max_length=255,default='Unknown')
    email=models.EmailField(max_length=320,default='Unknown')
    address=models.TextField(default='Unknown')
    mobile_number=models.CharField(max_length=255,default='Unknown')