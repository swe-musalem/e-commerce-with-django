from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.auth import views as authentication_view
# namespacing for this app
app_name = 'users'

"""root url myapp/ """

urlpatterns = [
    path('register/',views.register),
    # login in django is pre-defined use it directly , this pre-defined login view will look for login.html template
    path('login/',authentication_view.LoginView.as_view(template_name='users/login.html'),name='login'),
    # logging out is completly handled by django 
    path('logout/',authentication_view.LogoutView.as_view(template_name='users/logout.html'),name='logout'),
    path('profile/', views.profile , name='profile'),
    path('createprofile/',views.createProfile, name='createProfile'),
    path('sellerProfile/<int:id>/',views.sellerProfile,name='sellerProfile')
    
]   
