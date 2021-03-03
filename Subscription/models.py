from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Course(models.Model):
    course_name = models.CharField(max_length=200)
    course_id = models.CharField(max_length=20)
    premium = models.BooleanField(default=True)

    
    def __str__(self):
        return self.course_name

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    stripeid = models.CharField(max_length=255)
    stripe_subscription_id = models.CharField(max_length=255)
    cancel_at_period_end = models.BooleanField(default=False)
    membership = models.BooleanField(default=False)