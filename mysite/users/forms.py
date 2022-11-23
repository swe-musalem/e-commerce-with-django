from dataclasses import fields
from django.contrib.auth.forms import UserCreationForm 
#                                     the class which will be inherted to our own class 
from django.contrib.auth.models import User
# django provides a pre-defined model, no need to create new
from django import forms


# edit the layout of the input field next to required 
class NewUserForm(UserCreationForm):
    username = forms.CharField(required=True , widget=forms.TextInput(attrs={'class':'focus:outline-none w-full '}))
    email = forms.EmailField(required=True , widget=forms.EmailInput(attrs={'class':'focus:outline-none w-full '}))
    password1 = forms.CharField(required=True, widget=forms.PasswordInput(attrs={'class':'focus:outline-none w-full '}))
    password2 = forms.CharField(required=True, widget=forms.PasswordInput(attrs={'class':'focus:outline-none w-full '}))

    class Meta:
        # add a Meta class to which has two functions:
            # 1) To indicate which model we are using which in this case is the default user model
        model = User
        # 2) To show which fields we want to include in our final form and what order they should be rendered on our page
        fields = ("username","email","password1","password2")


    # method which saves the users info
    # self here refers to the class attributes insted of passing them all
    def save(self,commit=True):
        user = super(NewUserForm,self).save(commit=False)
        user.email = self.cleaned_data['email']

        if commit:
            user.save()
        return user