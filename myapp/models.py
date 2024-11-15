from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profiles')
    name = models.CharField(max_length=100)
    profile = models.ImageField(upload_to='profile', default='profile/default.webp')

    def __str__(self):
        return self.name
