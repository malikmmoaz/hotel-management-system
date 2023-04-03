# import django models
from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser


class Guest(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    
    def __str__(self):
        return f'Guest: {self.user.first_name}'
