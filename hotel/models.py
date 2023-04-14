# import django models
from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser


class HotelManager(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    
    def __str__(self):
        return f'Hotel Manager: {self.user.first_name}'

class HotelApplication(models.Model):
    hotel_manager = models.ForeignKey(HotelManager, null=True, on_delete=models.SET_NULL)
    hotel_name = models.CharField(max_length=100)
    hotel_address = models.CharField(max_length=100)
    hotel_contact = models.CharField(max_length=100)
    hotel_email = models.CharField(max_length=100)
    hotel_description = models.CharField(max_length=100)
    hotel_image = models.FileField(upload_to=f'applications/')
    hotel_status = models.BooleanField(default=False)
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)

    # if hotel status true create hotel object
    def save(self, *args, **kwargs):
        if self.hotel_status:
            hotel = Hotel.objects.create(
                hotel_manager = self.hotel_manager,
                hotel_name = self.hotel_name,
                hotel_address = self.hotel_address,
                hotel_contact = self.hotel_contact,
                hotel_email = self.hotel_email,
                hotel_description = self.hotel_description,
                hotel_image = self.hotel_image,
                latitude = self.latitude,
                longitude = self.longitude,
            )
            hotel.save()
        super(HotelApplication, self).save(*args, **kwargs)

    def __str__(self):
        return "application for: " + self.hotel_name + " by Manager " + self.hotel_manager.user.first_name

class Hotel(models.Model):
    hotel_manager = models.ForeignKey(HotelManager, null=True, on_delete=models.SET_NULL)
    hotel_name = models.CharField(max_length=100)
    hotel_address = models.CharField(max_length=100)
    hotel_contact = models.CharField(max_length=100)
    hotel_email = models.CharField(max_length=100)
    hotel_description = models.CharField(max_length=100)
    hotel_image = models.FileField(upload_to=f'hotels/{hotel_name}', null=True)
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)

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
        return f'{self.room_type} @ {self.hotel.hotel_name}'

class Room(models.Model):
    room_number = models.CharField(max_length=100)
    room_type = models.ForeignKey(RoomType, on_delete=models.CASCADE)
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.room_number} {self.room_type.room_type} @ {self.hotel.hotel_name}'

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

# add guest user to this model + alot room :)
class RoomBooking(models.Model):
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    room_type = models.ForeignKey(RoomType, on_delete=models.CASCADE, null=True)
    check_in = models.DateField()
    check_out = models.DateField()
    booking_date = models.DateField(auto_now_add=True)
    is_cancelled = models.BooleanField(default=False)
    checked_out = models.BooleanField(default=False, null=True)
    check_out_time = models.TimeField(null=True)
    housekeeping_required = models.BooleanField(default=False, null=True)

    def __str__(self):
        return f'{self.hotel.hotel_name} | {self.room_type.room_type} @ {self.check_in} - {self.check_out}'

class HotelReview(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    review = models.TextField()
    rating = models.IntegerField()
    review_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.user.username