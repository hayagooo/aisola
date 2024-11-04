from django.db import models
import random
import string
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

def generateKey():
    return ''.join(random.choices(string.digits, k=6))

def generateToken():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=60))

class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.key = generateKey()
        user.token = generateToken()
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)


class User(AbstractBaseUser):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    key = models.CharField(max_length=6, unique=True, default=generateKey)
    token = models.CharField(max_length=60, unique=True, default=generateToken)
    password = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='user_photos/', blank=True, null=True)
    level = models.CharField(max_length=50)
    verified_at = models.DateTimeField(blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']