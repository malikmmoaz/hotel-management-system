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

# Create your views here.
def home(request):
    return render(request, 'home.html')

def registerHotel(request):
    form = CreateHotelForm()
    if request.method == 'POST':
        form = CreateHotelForm(request.POST)
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
            HotelManager.objects.create(user=user)
            messages.success(request, 'Account was created successfully')
            return redirect('login')
    context = {'form': form}
    return render(request, 'register.html', context)

def loginHotel(request):
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

def logoutHotel(request):
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


# creates hotel_application object, post hotel_status == True, hotel object is created
def hotel_application(request):
    form = HotelApplicationForm()
    if request.method == 'POST':
        form = HotelApplicationForm(request.POST, request.FILES)
        if form.is_valid():
            hotel_application = form.save(commit=False)
            hotel_application.hotel_manager = HotelManager.objects.get(user=request.user)
            hotel_application.save()
            # messages.success(request, 'Your application was successfully submitted!')
            return HttpResponse('hotel application submitted')
    context = {'form': form}
    return render(request, 'hotel_application.html', context)

# check for specific hotel also
def isRoomTypeAvailable(roomType, checkInDate, checkOutDate):
    bookings = RoomBooking.objects.filter(room_type=roomType)
    rooms_count = Room.objects.filter(room_type=roomType).count()
    bookings_count = 0
    for booking in bookings:
        if checkInDate <= booking.check_out and checkOutDate >= booking.check_in:
            bookings_count += 1
    if bookings_count >= rooms_count:
        return False
    return True

def book_room(request):
    form = RoomBookingForm()
    if request.method == 'POST':
        form = RoomBookingForm(request.POST)
        hotel_manager = HotelManager.objects.get(user=request.user)
        hotel_name = HotelApplication.objects.get(hotel_manager=hotel_manager).hotel_name
        if form.is_valid():
            print(f'is room type available: {isRoomTypeAvailable(form.cleaned_data["room_type"], form.cleaned_data["check_in"], form.cleaned_data["check_out"])}')
            if isRoomTypeAvailable(form.cleaned_data["room_type"], form.cleaned_data["check_in"], form.cleaned_data["check_out"]):
                room_booking = form.save(commit=False)
                room_booking.hotel = Hotel.objects.get(hotel_name=hotel_name)
                room_booking.save()
                messages.success(request, 'Your room was successfully added!')
            else:
                messages.error(request, 'Room is not available for the selected dates.')
    context = {'form': form}
    return render(request, 'book_room.html', context)

def update_booking(request, pk):
    booking = RoomBooking.objects.get(id=pk)
    form = RoomBookingForm(instance=booking)
    if request.method == 'POST':
        form = RoomBookingForm(request.POST, instance=booking)
        if form.is_valid():
            form.save()
            return redirect('bookings')
    context = {'form': form}
    return render(request, 'update_booking.html', context)

def delete_booking(request, pk):
    booking = RoomBooking.objects.get(id=pk)
    booking.is_cancelled = True
    booking.save()
    return redirect('bookings')

def checkout(request, pk):
    booking = RoomBooking.objects.get(id=pk)
    booking.checked_out = True
    booking.check_out_time = datetime.now()
    booking.save()
    return redirect('bookings')

def bookings(request):
    hotel_manager = HotelManager.objects.get(user=request.user)
    hotel_name = HotelApplication.objects.get(hotel_manager=hotel_manager).hotel_name
    hotel = Hotel.objects.get(hotel_name=hotel_name)
    bookings = RoomBooking.objects.filter(hotel=hotel)
    context = {'bookings': bookings, 'hotel': hotel}
    return render(request, 'bookings.html', context)




















# make a view for displaying all time statistics 
def hotel_dashboard(request):
    curr_hotel = request.user.hotel
    # total number of rooms available in the hotel
    available_rooms = curr_hotel.room_set.filter(room_available=True).count()
    # total number of rooms currently booked in the hotel 
    booked_rooms = curr_hotel.room_set.filter(room_available=False).count()
    # total number of guests currently in the hotel
    # total number of guests who have checked out of the hotel
    # total revenue generated by the hotel
    # a list displaying details of each guest that checked in the hotel
    

    # print(request.user.id)
    return HttpResponse("Hello")
    