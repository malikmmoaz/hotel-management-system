# import django models
from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser


class HotelManager(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.user.first_name

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

class Hotel(models.Model):
    hotel_name = models.CharField(max_length=100)
    hotel_address = models.CharField(max_length=100)
    hotel_contact = models.CharField(max_length=100)
    hotel_email = models.CharField(max_length=100)
    hotel_description = models.CharField(max_length=100)

    def __str__(self):
        return self.hotel_name

class HotelImage(models.Model):
    hotel_image = models.FileField(upload_to=f'hotels/')
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)

    def __str__(self):
        return self.hotel.hotel_name

class RoomType(models.Model):
    room_type = models.CharField(max_length=100)
    room_capacity = models.CharField(max_length=100)
    room_description = models.CharField(max_length=100)
    room_price = models.CharField(max_length=100)
    room_image = models.FileField(upload_to=f'rooms/')
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)

    def __str__(self):
        return self.room_type

class Room(models.Model):
    room_number = models.CharField(max_length=100)
    room_available = models.BooleanField(default=True)
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    room_type = models.ForeignKey(RoomType, on_delete=models.CASCADE)

    def __str__(self):
        return self.hotel.hotel_name + " " + self.room_number

class Amenities(models.Model):
    amenity_name = models.CharField(max_length=100)
    amenity_description = models.CharField(max_length=100)
    amenity_image = models.FileField(upload_to=f'amenities/')
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)

    def __str__(self):
        return self.amenity_name

class Facilities(models.Model):
    facility_name = models.CharField(max_length=100)
    facility_description = models.CharField(max_length=100)
    facility_image = models.FileField(upload_to=f'facilities/')
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)

    def __str__(self):
        return self.facility_name

class HotelBooking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    check_in = models.DateField()
    check_out = models.DateField()
    booking_date = models.DateField(auto_now_add=True)
    booking_status = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username

class HotelReview(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    review = models.TextField()
    rating = models.IntegerField()
    review_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.user.username