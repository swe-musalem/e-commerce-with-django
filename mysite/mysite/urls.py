"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
"""

from django.contrib import admin
from django.urls import path , include
from django.conf import settings
from django.conf.urls.static import static
from myapp import views

"""
    best practies is put each app it's own urlpattern 

    when ever the url starts with myapp/ redirect it to myapp.urls

    ---------create admin user---------

    python manage.py createsuperuser
"""
urlpatterns = [
    path('admin/', admin.site.urls),
    path('myapp/',include('myapp.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)