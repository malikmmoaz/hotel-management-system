from django.shortcuts import render, HttpResponse
from django.shortcuts import render, redirect, HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .models import *
from .forms import *
from django.core.mail import send_mail
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from django.contrib.auth.models import User
from django.core import validators
from django.db.models import Sum
from datetime import datetime, timedelta
from hotel.models import Hotel, HotelImage
from hotel.forms import RoomBookingForm


# Create your views here.
def main(request):
    return render(request, 'main.html')

def registerGuest(request):
    form = CreateGuestForm()
    if request.method == 'POST':
        form = CreateGuestForm(request.POST)
        email = request.POST.get("email")
        try:
            validators.validate_email(email)
        except validators.ValidationError:
            messages.error(request, "Invalid email format.")
            return HttpResponseRedirect(reverse('register'))
        if User.objects.filter(email=request.POST['email']).exists():
            messages.error(request, 'Email already exists. Please either login with this email or register with a new email.')
            return HttpResponseRedirect(reverse('register'))
        if form.is_valid():
            user = form.save()
            Guest.objects.create(user=user)
            messages.success(request, 'Account was created successfully')
            return redirect('login')
    context = {'form': form}
    return render(request, 'register.html', context)

def loginGuest(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is None:
            messages.info(request, 'Email OR password is incorrect')
        else:
            login(request, user)
            return HttpResponseRedirect(reverse('home'))
    return render(request, 'login.html')

def logoutGuest(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))

def change_password(request):
    if request.method == 'POST':
        form = Password_Change_Form(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            password = user.password
            messages.success(request, 'Your password was successfully updated!')
            return redirect('home')
        else:
            messages.info(request, 'Please correct the error below.')
    else:
        form = Password_Change_Form(request.user)
    return render(request, 'change_password.html', {'form': form})

def browse_hotels(request):
    hotels = list(Hotel.objects.values('hotel_name', 'latitude', 'longitude'))
    hotels_  = Hotel.objects.all()
    context = {'hotels_': hotels_, 'hotels': hotels}
    return render(request, 'browse_hotels.html', context)

def hotel_listing(request, pk):
    hotels = list(Hotel.objects.filter(id=pk).values('hotel_name', 'latitude', 'longitude'))
    hotel = Hotel.objects.get(id=pk)
    hotel_image_1 = HotelImage.objects.filter(hotel=hotel).last()
    hotel_image_2 = HotelImage.objects.filter(hotel=hotel).first()
    context = {'hotels': hotels, 'hotel': hotel, 'hotel_image_1': hotel_image_1, 'hotel_image_2': hotel_image_2}
    return render(request, 'hotel_listing.html', context)

# def online_reservation(request, pk):
#     form = RoomBookingForm(hotel=Hotel.objects.get(id=pk))
#     if request.method == 'POST':
#         form = RoomBookingForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('home')
#     context = {'form': form}
#     return render(request, 'online_reservation.html', context)