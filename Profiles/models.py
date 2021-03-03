from django.db import models
from django.contrib.auth.models import User
from PIL import Image

# Create your models here.
class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    full_name = models.CharField(max_length=200, null=False)
    image = models.ImageField( upload_to='profilepics', null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    


    def __str__(self):
        return f'{self.user.username} Profile'

class Tutor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    full_name = models.CharField(max_length=200, null=False)
    image = models.ImageField(default='profilepics/default.jpg', upload_to='profilepics')
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return f'{self.user.username} Profile'


