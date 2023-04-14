from django.forms import ModelForm, widgets
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.contrib.auth.models import User
from django import forms
from .models import *
from django.db.models import Q, F

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
    old_password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'input', 'type': 'password'}))
    new_password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'input', 'type': 'password'}))
    new_password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'input', 'type': 'password'}))
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
            'latitude': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Latitude'}),
            'longitude': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Longitude'}),
        }

class HotelForm(ModelForm):
    class Meta:
        model = Hotel
        fields = '__all__'
        exclude = ['hotel_manager']
        widgets = {
            'hotel_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Hotel Name'}),
            'hotel_address': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Hotel Address'}),
            'hotel_contact': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Contact Number'}),
            'hotel_email': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Hotel Email'}),
            'hotel_description': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Hotel Description'}),
            'latitude': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Latitude'}),
            'longitude': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Longitude'}),
        }

class RoomBookingForm(ModelForm):
    # def __init__(self, bookings=None, *args, **kwargs):
    #     super(RoomBookingForm, self).__init__(*args, **kwargs)
    #     if bookings is not None:
    #         # exclude rooms that are booked during any of the bookings
    #         exclude_q = Q()
    #         for booking in bookings:
    #             exclude_q |= Q(roombooking__check_in__lt=booking.check_out, roombooking__check_out__gt=booking.check_in, room=F('id'))
    #         self.fields['room'].widget = Room.objects.filter(hotel__in=bookings.values('hotel')).exclude(exclude_q)
    #     else:
    #         # show all rooms
    #         self.fields['room'].queryset = Room.objects.all()
    class Meta:
        model = RoomBooking
        fields = '__all__'
        exclude = ['hotel', 'booking_date', 'checked_out', 'check_out_time', 'is_cancelled', 'housekeeping_required']
        widgets = {
            'check_in': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'Check In', 'type': 'date'}),
            'check_out': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'Check Out', 'type': 'date'}),
            'room': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Room'}),
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

class RoomForm(ModelForm):
    class Meta:
        model = Room
        fields = '__all__'
        exclude = ['hotel']
        widgets = {
            'room_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Room Number'}),
            'room_type': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Room Type'}),
        }

class HotelImageForm(ModelForm):
    class Meta:
        model = HotelImage
        fields = '__all__'
        exclude = ['hotel']
        widgets = {
            'hotel_image': forms.FileInput(attrs={'class': 'form-control', 'placeholder': 'Hotel Image'}),
        }