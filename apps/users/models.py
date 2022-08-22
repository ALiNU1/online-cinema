from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    username = models.CharField(max_length=150)
    email = models.EmailField(max_length=200, blank=True, null=True)
    profile_image = models.ImageField(upload_to = "profile_image/")
    phone= models.CharField(max_length=100)
    
    def __str__(self):
        return self.username

    class Meta:
        verbose_name="Пользователь"
        verbose_name_plural="Пользователи"