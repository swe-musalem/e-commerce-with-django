from django.contrib import admin
from django.urls import path
from . import views



"""root url myapp/ """
urlpatterns = [
    path('app/',views.index),
    path('products/',views.products),
    #specify the data type and send it to the parameter in the view function
    path('products-detail/<int:id>/', views.product_detail),
]
