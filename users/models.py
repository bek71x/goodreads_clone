from django.contrib.auth.models import AbstractUser
from django.db import models



class CustomUser(AbstractUser):
    profile_picture = models.ImageField(default='profile_pictures/default.png', upload_to='profile_pictures')
    gender = models.CharField(max_length=10,choices=(('Male','Erkak'),('Female','Ayol')),default='Male')

    def get_full_name(self):
        return self.first_name + ' ' + self.last_name