from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Course(models.Model):
    course_title = models.CharField(max_length=255, null=True)
    course_description = models.CharField(max_length=255, null=True)
    thumbnail = models.ImageField(upload_to='course_thumbnails', null=True)
    premium = models.BooleanField(default=True)

    
    def __str__(self):
        return self.course_title

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    stripeid = models.CharField(max_length=255)
    stripe_subscription_id = models.CharField(max_length=255)
    cancel_at_period_end = models.BooleanField(default=False)
    membership = models.BooleanField(default=False)