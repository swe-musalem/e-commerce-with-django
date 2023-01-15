
from django.shortcuts import render ,redirect
from .models import Product ,homeImages
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy

"""
all the products will be shown at myapp/index.html

then when clicking on the link will navigate to /myapp/detail.html/{{ product.id }}

the id is passed through the link

"""

def products(request):
    products = Product.objects.all()
    homeimages = homeImages.objects.all()
    context = {
        "products":products,
        "homeimages":homeimages,
        "homeImagesCount":homeimages.count(),
    }
    
    return render(request, 'myapp/index.html',context)

# convertd to CBV below

# ListView => give you all objects n
# class ProductListview(ListView):
#     model = Product
#     template_name = 'myapp/index.html'
#     def get_queryset(self):
#         '''
#         this line below is pre-defined, but we override this function so we need to put super in order to keep it and make new changes ^_^ 
#         '''
#         qs = super(ProductListview, self).get_queryset()
#         qs = qs.order_by('-id')
#         print(qs)
#         return qs
        
#     '''
#     whats happining is something like

#     context = {
#         get_queryset: context_object_name
#     }
#     '''
#     context_object_name = 'products'

"""

accesing the details of the product through url/id:
    myapp/product/{id}


"""

# def product_detail(request,id):
#     product = get_object_or_404(Product,id=id)
    
    
    
#     context = {
#         'product': product
#     }
#     return render(request,'myapp/detail.html',context)

class ProductDetailView(DetailView):
    model = Product
    template_name = 'myapp/detail.html'
    # there is an object and this class is able to access it but you have to specify the context_object_name
    context_object_name = 'product'


# @login_required
# def addProduct(request):
    
#     if request.method == "POST":
#         # print("x")\n
#         # get parameter are the name and id from the template
#         name = request.POST.get('name')
#         price = request.POST.get('price')
#         desc = request.POST.get('desc')
#         seller_name = request.user
        
#         # images cannot be posted
#         image = request.FILES['upload']
#         # so far these data are not stored to db
#         product = Product(name=name,price=price,desc=desc,image=image,seller_name=seller_name)
#         product.save()
        

#         import requests

#         r = requests.post("https://sheetdb.io/api/v1/106hkqvnar7mu", headers={}, json={"data": { "name":name,"price":price,"id":product.id } })

#         if r.status_code != 201:
#              print("error")
	

#     return render(request,'myapp/addproduct.html')

# class based view on addProduct


class ProductCreateView(CreateView):
    model = Product
    
    fields = ['name','price','desc','image']
    
    # Product.seller_name = 

def updateProduct(request,id):
    """
    the user sent 3 as id
    we store the data of the id in product which means we hav access on this id only
    when user send a post request we catch the values and assign it to the id 3


    """
    product = get_object_or_404(Product,id=id)
    context = { 'product': product }
    return render(request,'myapp/updateProduct.html',context)
    # try:
    #     product = Product.objects.get(id=id)
    #     context = { 'product': product } # get the data ato the form
    #     if request.method == "POST":
    #         # overwriting the exisiting objects from the form request 
    #         product.name = request.POST.get('name')
    #         product.price = request.POST.get('price')
    #         product.desc = request.POST.get('desc')
        
    #         product.image = request.FILES['upload']
    #         product.save()
    #         return redirect('/myapp/products')
    #     return render(request,'myapp/updateProduct.html',context)
        
    
    # except ObjectDoesNotExist as error:
    #     context = {
    #         'errorName':error,
    #         'errorDesc':'this occurs when querying about deleted product or doesn\'t exist',
    #         'errorCode':'204',
            
    #     }
    #     # in the same url return different template so no need for url
    #     return render(request,'myapp/errorPage.html',context)

class ProductUpdateView(UpdateView):
    model = Product
    
    fields = ['name','price','desc','image']
    template_name_suffix = "_update_form"
    
class ProductDeleteview(DeleteView):
    model = Product
    success_url = reverse_lazy("myapp:products")
    


def user_listing(request):
    product = Product.objects.filter(seller_name=request.user)

    context = {
        'product':product
    }
    return render(request,'myapp/userListing.html',context)