
from django.urls import path,include
from django.contrib import admin
from myapp import views

urlpatterns=[
    path("admin/", admin.site.urls),
    path("add_products/",views.add_products,name='add_products'),
    path("list/",views.list_products,name="list_products"),
    path("desc/",views.descending,name='descending'),
    path("created/",views.ordered_within_7_days,name="ordered_within_7_days"),
    path("price_range/",views.price_range,name="price_range"),
    path("keyword/",views.keyword,name="keyword")
]
