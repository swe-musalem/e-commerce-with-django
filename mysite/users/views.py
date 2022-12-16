from multiprocessing import context
from django.shortcuts import render , redirect
from .forms import NewUserForm
from .models import Profile
from django.contrib.auth.decorators import login_required
# Create your views here.

def register(request):
   # regular user visits the page
   form = NewUserForm()
   context = {
       'form':form,
    }
    
   # making a post request
   if request.method == 'POST':
      form = NewUserForm(request.POST)
      formErrors = form.errors
      # checks if valid redirect to login
      if form.is_valid():
         print("is_valid")
         user = form.save()
         return redirect('/users/login')
         # not valid render the same page with diffrent context
      else:
         return render(request,'users/register.html',{ 'form':form, 'formErrors':formErrors  })
         
          
  


   return render(request,'users/register.html',context)

@login_required
# if you are not logged in  you will be redirected to the specifc url in LOGIN_URL='<url>' to log in and see the page 
def profile(request):
   return render(request , 'users/profile.html')

def createProfile(request):
   if request.method == 'POST':
      connect_number = request.POST.get('connect_number')
      image = request.FILES['upload']
      user = request.user
      profile = Profile(user=user , connect_number = connect_number , image = image)
      profile.save()
   return render(request , 'users/createProfile.html')