from django.contrib import admin
from django.urls import path
from . import views

# namespacing for this app
app_name = 'myapp'

"""root url myapp/ """
urlpatterns = [
    path('app/',views.index),
    path('products/',views.products, name='products'),
    #specify the data type and send it to the parameter in the view function
    path('products_detail/<int:id>/', views.product_detail, name='products_detail'),
    path('products/add',views.addProduct,name='add_product'),
    path('products/update/<int:id>/',views.updateProduct,name='update_product')
    
]
