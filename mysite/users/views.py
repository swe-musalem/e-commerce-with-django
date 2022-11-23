from multiprocessing import context
from django.shortcuts import render , redirect
from .forms import NewUserForm
# Create your views here.

def register(request):
   
   
   if request.method == 'POST':
      form = NewUserForm(request.POST)
      if form.is_valid():
         print("is_valid")
         user = form.save()
         return redirect('/users/register')
   form = NewUserForm()
   print("is_valid 2")
   context = {
       'form':form
    }


   return render(request,'users/register.html',context)
