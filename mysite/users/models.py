from django.db import models
from django.contrib.auth.models import User
# Create your models here.


"""
here comes the forigenKey use because we want to attach diffrent tabels together

assume attaching User table with Product table we make use of User's primarykey and add it as forigenkey in Product table

you can make use of one-to-one relation instead of using a forigenkey * better to know the diffrence * 

"""

# every user has a profile
class Profile(models.Model):
    def __str__(self) -> str:
        # self.user is object
        return self.user.username
    # 'to' and 'on_delete' required arguments for user
        # on_delete=models.CASCADE -> this means that if any user is deleted the profile attached to it should be deleted
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    image = models.ImageField(default='profile.jpg',upload_to='profile_pictures')
    connect_number = models.CharField(max_length=10,default='0')