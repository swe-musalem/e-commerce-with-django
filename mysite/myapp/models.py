from distutils.command.upload import upload

from django.db import models
from django.contrib.auth.models import User
# Create your models here.

"""
remebmer to add "myapp" to installed apps

not a real sql code until you do migration

commands:
    python manage.py makemigrations
        then:
                python manage.py migrate

to see the table at admin pannel you have to register at admin file


"""

class Product(models.Model):
    
    name = models.CharField(max_length=100 , blank=False)
    price = models.IntegerField(blank=False)
    desc = models.TextField(max_length=200, blank=True)
    seller_name = models.ForeignKey(User,on_delete=models.CASCADE, default=1)
                            # you need to set media root and media url
    image = models.ImageField(blank=True, upload_to='images')
    def __str__(self):
        return self.name
