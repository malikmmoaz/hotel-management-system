from django.forms import ModelForm, widgets
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.contrib.auth.models import User
from django import forms
from .models import *

class CreateHotelForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2']

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
        exclude = ['user', 'hotel', 'booking_date']
        widgets = {
            'check_in': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'Check In', 'type': 'date'}),
            'check_out': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'Check Out', 'type': 'date'}),
            'room': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Room'}),
        }