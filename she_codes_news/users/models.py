from django.db import models

from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import Users


# Create your models here.
class CustomUser(AbstractUser):
    pass
    def __str__(self):
        return self.username


# # Extending User Model Using a One-To-One Link
# class UserPage(Users):
#     user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
#     avatar = models.ImageField(default='default.jpg', upload_to='profile_images')
#     bio = models.TextField()

#     def __str__(self):
#         return self.user.username