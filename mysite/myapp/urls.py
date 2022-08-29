from django.contrib import admin
from django.urls import path
from . import views

# namespacing for this app
app_name = 'myapp'

"""root url myapp/ """
urlpatterns = [
    path('app/',views.index),
    path('products/',views.products),
    #specify the data type and send it to the parameter in the view function
    path('products-detail/<int:id>/', views.product_detail, name='product_detail'),
]
