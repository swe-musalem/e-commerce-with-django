from django.contrib import admin
from django.urls import path
from . import views

# namespacing for this app
app_name = 'users'

"""root url myapp/ """
urlpatterns = [
    path('register/',views.register),
    
]
