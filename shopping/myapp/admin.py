from django.contrib import admin
from .models import Product
from .models import Author
from .models import Books
from .models import Genre

# Register your models here.
admin.site.register(Product)
admin.site.register(Author)
admin.site.register(Genre)
admin.site.register(Books)