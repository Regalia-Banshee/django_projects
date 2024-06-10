from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.http import JsonResponse
from .models import Product
from .models import Author
from .models import Books
from .models import Genre
from django.contrib import admin
from datetime import datetime,timedelta
import sys

'''def add_products(request):
    product1= Product(name='Iphone', price='999.00', category='Electronics')
    product2= Product(name='Xioami', price = '200.00',category="Electronics")
    product1.save()
    product2.save()
    print(f"Products {product1.name},{product2.name} added to database successfully",file=sys.stdout)
    return HttpResponse(f"Products {product1.name},{product2.name} added to database successfully")

def list_products(request):
    product=Product.objects.all()
    for elements in product:
        print(f"name:{elements.name},price:{elements.price},category:{elements.category}",file=sys.stdout)
    return HttpResponse(f"List Displayed in terminal")

def descending(request):
    product=Product.objects.order_by("-price")
    for element in product:
        print(f"Name:{element.name},price:{element.price}",file=sys.stdout)
    return HttpResponse("Output given in terminal")

def ordered_within_7_days(request):
    last_week=datetime.now()-timedelta(days=7)
    product=Product.objects.filter(created_at=last_week)
    for element in product:
        print(f"name:{element.name}",file=sys.stdout)
    return HttpResponse("Output given in terminal")

def price_range(request):
    min_price=100
    max_price=300
    product=Product.objects.filter(price__gte=min_price,price__lte=max_price)
    for element in product:
        print(f"name:{element.name},price:{element.price}",file=sys.stdout)
    return HttpResponse(f"Output given in terminal for object between {min_price} and {max_price} ")

def keyword(request):
    keyword="iph"
    product=Product.objects.filter(name__icontains=keyword)
    for element in product:
        print(f"name:{element.name},price:{element.price},category:{element.category}",file=sys.stdout)
    return HttpResponse("Output given in terminal")'''

def add_author(request):
    date1 = datetime.strptime('1964-06-24', '%Y-%m-%d').date()
    date2 = datetime.strptime('1897-08-11', '%Y-%m-%d').date()
    date3 = datetime.strptime('1934-05-19', '%Y-%m-%d').date()
    dan=Author(name='Dan Brown',birth_date=date1,nationality="American")
    enid=Author(name='Enid Blyton',birth_date=date2,nationality='British')
    ruskin=Author(name='Ruskin Bond',birth_date=date3,nationality='Indian')
    
    dan.save()
    enid.save()
    ruskin.save()
    return HttpResponse(f"Authors {dan},{enid},{ruskin} added to Database")

def add_genre(request):
    genre1=Genre(name='Thriller')
    genre2=Genre(name='Adventure')
    genre3=Genre(name='Fiction')
    
    genre1.save()
    genre2.save()
    genre3.save()
    return HttpResponse(f"Genre{genre1},{genre2},{genre3} added to Database")

def add_books(request):

    dan = Author.objects.get(name='Dan Brown')
    enid = Author.objects.get(name='Enid Blyton')
    ruskin = Author.objects.get(name='Ruskin Bond')

    genre1=Genre.objects.get(name='Thriller')
    genre2=Genre.objects.get(name='Adventure')
    genre3=Genre.objects.get(name='Fiction')
    
    book1=Books(name='Inferno',author=dan,price='30.00')
    book2=Books(name='Angels and Demons',author=dan,price='15.00')
    book3=Books(name='Secret Seven',author=enid,price='5.00')
    book4=Books(name='Famous Five',author=enid,price='3.00')
    book5=Books(name='The last Tiger',author=ruskin,price="1.00")
    book6=Books(name="Angry River",author=ruskin,price="1.00")
    
    book1.save()
    book2.save()
    book3.save()
    book4.save()
    book5.save()
    book6.save()

    book1.genre.set([genre1])
    book2.genre.set([genre1])
    book3.genre.set([genre2])
    book4.genre.set([genre2])
    book5.genre.set([genre3])
    book6.genre.set([genre3])
    return HttpResponse(f"Books added to Database")

def specific_author(request):
    spec_author=Books.objects.filter(author__name="Dan Brown")
    for books in spec_author:
        print(f"{books.name}",file=sys.stdout)
    return HttpResponse(f"Output in terminal")

def get_authors_by_genre(request):
    authors = Author.objects.filter(books__genre__name="Thriller").distinct()
    for author in authors:
        print(f"{author.name}")
    return HttpResponse(f"{author.name}")

def update_price(request):
    book=Books.objects.get(id=1)
    new_price='40.00'
    book.price=new_price
    book.save()
    return HttpResponse(f"price of {book.name} upadated to {book.price}")
