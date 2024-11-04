from django.db import models

class User(models.Model):
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