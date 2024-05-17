"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from myapp.views import welcome
from myapp.views import ProfileView
from myapp.views import get_profile_by_name
from myapp.views import update_email
from myapp.views import update_name
from myapp.views import Delete_Profile
urlpatterns = [
    path("admin/", admin.site.urls),
    path("espanol/", welcome, name="welcome"),
    path("name/",ProfileView,name="profile"),
    path("profile/<str:name>/",get_profile_by_name,name="get_profile_by_name"),
    path("profile/<str:name>/email",update_email,name="update_email"),
    path("profile/<str:name>/update",update_name,name="update_name"),
    path("profile/<str:name>/delete",Delete_Profile,name="Delete_Profile")
] 
