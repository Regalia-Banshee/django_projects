from django.db import models

class Product(models.Model):
   name = models.CharField(max_length=255)
   price = models.DecimalField(max_digits=8,decimal_places=2)
   category=models.CharField(max_length=255)
   created_at=models.DateTimeField(auto_now_add=True)

class Author(models.Model):
   name=models.CharField(max_length=255)
   birth_date=models.DateField()
   nationality=models.CharField(max_length=255)


class Genre(models.Model):
   name=models.CharField(max_length=255)

class Books(models.Model):
   name=models.CharField(max_length=255)
   author=models.ForeignKey(Author, on_delete=models.CASCADE)
   genre=models.ManyToManyField(Genre)
   publication_date=models.DateField(null=True,blank=True)
   price=models.DecimalField(max_digits=8,decimal_places=2)


   