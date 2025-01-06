from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    ADMIN = 'admin' 
    STAFF = 'staff' 
    CATEGORY_CHOICES = [ (ADMIN, 'Admin'), (STAFF, 'Staff'), ]
    phone=models.CharField(max_length=13,unique=True)
    category = models.CharField( max_length=5, choices=CATEGORY_CHOICES, default=STAFF)
    date_joined = models.DateTimeField(auto_now_add=True)

