from django.db import models
import random
import string
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

def generate_key():
    return ''.join(random.choices(string.digits, k=6))

def generate_token():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=60))

class User(AbstractBaseUser):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    key = models.CharField(max_length=255, unique=True)
    token = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255, unique=True)
    photo = models.ImageField(upload_to='user_photos/', blank=True, null=True)
    level = models.CharField(max_length=255)
    verified_at = models.DateTimeField(blank=True, null=True)
    joined_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name