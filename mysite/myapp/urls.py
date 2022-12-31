from django.contrib import admin
from django.urls import path
from . import views

# namespacing for this app
app_name = 'myapp'

"""root url myapp/ """
urlpatterns = [
    path('products/',views.ProductListview.as_view(), name='products'),
    #specify the data type and send it to the parameter in the view function
    # in class based view refere to the primary key parameter in url as pk
    path('products_detail/<int:pk>/', views.ProductDetailView.as_view(), name='products_detail'),
    path('products/add',views.addProduct,name='add_product'),
    path('products/update/<int:id>/',views.updateProduct,name='update_product'),
    path('userlisting/',views.user_listing, name='userlisting'),
]
