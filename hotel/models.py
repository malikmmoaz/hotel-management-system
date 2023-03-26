# import django models
from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser

class HotelApplication(models.Model):
    hotel_name = models.CharField(max_length=100)
    hotel_address = models.CharField(max_length=100)
    hotel_contact = models.CharField(max_length=100)
    hotel_email = models.CharField(max_length=100)
    hotel_description = models.CharField(max_length=100)
    hotel_image = models.FileField(upload_to=f'applications/')
    hotel_status = models.BooleanField(default=False)

    def __str__(self):
        return "application for: " + self.hotel_name