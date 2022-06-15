from django.db import models
from .models import Profile

from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User
from .models import Profile


# Create your models here.
class CustomUser(AbstractUser):
    pass
    def __str__(self):
        return self.username


# Extending User Model Using a One-To-One Link
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    avatar = models.ImageField(default='default.jpg', upload_to='profile_images')
    bio = models.TextField()

    def __str__(self):
        return self.user.username