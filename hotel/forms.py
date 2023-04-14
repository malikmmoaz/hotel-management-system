from django.forms import ModelForm, widgets
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.contrib.auth.models import User
from django import forms
from .models import *

class CreateHotelForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'input', 'placeholder': 'Username'}),
            'email': forms.TextInput(attrs={'class': 'input', 'placeholder': 'Email'}),
            'first_name': forms.TextInput(attrs={'class': 'input', 'placeholder': 'First Name'}),
            'last_name': forms.TextInput(attrs={'class': 'input', 'placeholder': 'Last Name'}),
            'password1': forms.PasswordInput(attrs={'class': 'input', 'placeholder': 'Password'}),
            'password2': forms.PasswordInput(attrs={'class': 'input', 'placeholder': 'Confirm Password'}),
        }

class Password_Change_Form(PasswordChangeForm):
    old_password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'type': 'password'}))
    new_password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'type': 'password'}))
    new_password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'type': 'password'}))
    class Meta:
        model = User
        fields = ['old_password', 'new_password1', 'new_password2']

class HotelApplicationForm(ModelForm):
    class Meta:
        model = HotelApplication
        fields = '__all__'
        exclude = ['hotel_manager', 'hotel_status']
        widgets = {
            'hotel_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Hotel Name'}),
            'hotel_address': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Hotel Address'}),
            'hotel_contact': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Contact Number'}),
            'hotel_email': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Hotel Email'}),
            'hotel_description': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Hotel Description'}),
            'hotel_image': forms.FileInput(attrs={'class': 'form-control', 'placeholder': 'Hotel Image'}),
        }

class RoomBookingForm(ModelForm):
    class Meta:
        model = RoomBooking
        fields = '__all__'
        exclude = ['hotel', 'booking_date', 'checked_out', 'check_out_time', 'is_cancelled', 'housekeeping_required']
        widgets = {
            'check_in': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'Check In', 'type': 'date'}),
            'check_out': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'Check Out', 'type': 'date'}),
            'room': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Room'}),
        }
        
class HotelForm(ModelForm):
    class Meta:
        model = Hotel
        fields = '__all__'
        exclude = ['hotel']
        widgets = {
            'hotel_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Hotel Name'}),
            'hotel_address': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Hotel Address'}),
            'hotel_contact': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Contact Number'}),
            'hotel_email': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Hotel Email'}),
            'hotel_description': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Hotel Description'}),
            'hotel_image': forms.FileInput(attrs={'class': 'form-control', 'placeholder': 'Hotel Image'}),
        }
        
class AmenitiesForm(ModelForm):
    class Meta:
        model = Amenities
        fields = '__all__'
        exclude = ['hotel']
        widgets = {
            'amenity_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Amenity Name'}),
            'amenity_description': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Amenity Description'}),
            'amenity_image': forms.FileInput(attrs={'class': 'form-control', 'placeholder': 'Amenity Image'}),
        }
        
class FacilityForm(ModelForm):
    class Meta:
        model = Facilities
        fields = '__all__'
        exclude = ['hotel']
        widgets = {
            'facility_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Facility Name'}),
            'facility_description': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Facility Description'}),
            'facility_image': forms.FileInput(attrs={'class': 'form-control', 'placeholder': 'Facility Image'}),
        }

class RoomTypeForm(ModelForm):
    class Meta:
        model = RoomType
        fields = '__all__'
        exclude = ['hotel']
        widgets = {
            'room_type': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Room Type'}),
            'room_capacity': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Room Capacity'}),
            'room_description': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Room Description'}),
            'room_price': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Room Price'}),
            'room_image': forms.FileInput(attrs={'class': 'form-control', 'placeholder': 'Room Image'}),
        }