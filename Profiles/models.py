from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from django.conf import settings

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

class Course(models.Model):
    course_name = models.CharField(max_length=200)
    course_id = models.CharField(max_length=20)
    
    def __str__(self):
        return self.course_name


class Unit(models.Model):
    unit_name = models.CharField(max_length= 60)
    unit_code = models.CharField(max_length=60)
    tutor_name = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='%(class)s_createdby', on_delete=models.CASCADE)
    tutor_contact = models.CharField(max_length=10)
    course_id = models.ManyToManyField(Course)


    def __str__(self):
        return self.unit_name


class Notes(models.Model):
    note = models.FileField(null = True, upload_to='notes')
    unit = models.ForeignKey(Unit, on_delete= models.CASCADE, null = True)  
    note_title = models.CharField(null=True,max_length=30)
    def __str__(self):
        return self.note_title


