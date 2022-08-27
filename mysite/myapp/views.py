from itertools import product
from multiprocessing import context
from django.shortcuts import render
from django.http import HttpResponse

from .models import Product


def index(request):
    return HttpResponse("somesing")


def products(request):
    products = Product.objects.all()
    
    context = {
        "products":products
    }
    
    return render(request, 'myapp/index.html',context)

"""

accesing the details of the product through url/id:
    myapp/product/{id}


"""

def product_detail(request,id):
    product = Product.objects.get(id=id)
    context = {
        'product': product 
    }
    return render(request,'myapp/detail.html',context)