from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.http import JsonResponse
from .models import Product
from django.contrib import admin
from datetime import datetime,timedelta
import sys

def add_products(request):
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
    return HttpResponse("Output given in terminal")