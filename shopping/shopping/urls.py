
from django.urls import path,include
from django.contrib import admin
from myapp import views

urlpatterns=[
    path("admin/", admin.site.urls),
    path("add_author/",views.add_author,name='add_author'),
    path("add_genre/",views.add_genre,name='add_genre'),
    path("add_books/",views.add_books,name='add_books'),
    path("specific_author",views.specific_author,name='specific_author'),
    path("get_authors_by_genre",views.get_authors_by_genre,name='get_authors_by_genre'),
    path("update_price",views.update_price,name='update_price')
]
