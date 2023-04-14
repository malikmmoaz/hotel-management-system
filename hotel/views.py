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

def registerHotelManager(request):
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

def loginHotelManager(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is None:
            messages.info(request, 'Username or password is incorrect.')
        else:
            login(request, user)
            if HotelApplication.objects.filter(hotel_manager=HotelManager.objects.get(user=user)).exists():
                hotel_application = HotelApplication.objects.get(hotel_manager=HotelManager.objects.get(user=user))
                if hotel_application.hotel_status:
                    return HttpResponseRedirect(reverse('hotel_details'))
            return HttpResponseRedirect(reverse('hotel_application'))
    return render(request, 'login.html')

def logoutHotelManager(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))

def change_password(request):
    if request.method == 'POST':
        form = Password_Change_Form(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            password = user.password
            messages.success(request, 'Your password was successfully updated.')
            return redirect('home')
        else:
            messages.info(request, 'Incorrect password. Please try again.')
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
            return HttpResponse('hotel application submitted')
    context = {'form': form}
    if HotelApplication.objects.filter(hotel_manager=HotelManager.objects.get(user=request.user)).exists():
        hotel_application = HotelApplication.objects.get(hotel_manager=HotelManager.objects.get(user=request.user))
        if hotel_application.hotel_status:
            return HttpResponseRedirect(reverse('hotel_details'))
        else:
            return render(request, 'application_pending.html', context)
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

def bookings(request):
    hotel_manager = HotelManager.objects.get(user=request.user)
    hotel_name = HotelApplication.objects.get(hotel_manager=hotel_manager).hotel_name
    hotel = Hotel.objects.get(hotel_name=hotel_name)
    bookings = RoomBooking.objects.filter(hotel=hotel)
    context = {'bookings': bookings, 'hotel': hotel}
    return render(request, 'bookings.html', context)

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
    booking.housekeeping_required = True
    booking.save()
    return redirect('bookings')

def housekeeping(request):
    hotel_manager = HotelManager.objects.get(user=request.user)
    hotel_name = HotelApplication.objects.get(hotel_manager=hotel_manager).hotel_name
    hotel = Hotel.objects.get(hotel_name=hotel_name)
    bookings = RoomBooking.objects.filter(hotel=hotel, housekeeping_required=True)
    context = {'bookings': bookings, 'hotel': hotel}
    return render(request, 'housekeeping.html', context)

def housekeeping_done(request, pk):
    booking = RoomBooking.objects.get(id=pk)
    booking.housekeeping_required = False
    booking.save()
    return redirect('housekeeping')

def update_hotel_details(request):
    hotel_manager = HotelManager.objects.get(user=request.user)
    hotel_application = HotelApplication.objects.get(hotel_manager=hotel_manager)
    form = HotelApplicationForm(instance=hotel_application)
    if request.method == 'POST':
        form = HotelApplicationForm(request.POST, request.FILES, instance=hotel_application)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {'form': form}
    return render(request, 'update_hotel_details.html', context)

def update_hotel_images(request):
    hotel_manager = HotelManager.objects.get(user=request.user)
    hotel = Hotel.objects.get(hotel_manager=hotel_manager)
    try:
        hotel_images = HotelImage.objects.filter(hotel=hotel)
    except:
        hotel_images = None
    form = HotelImageForm()
    if request.method == 'POST':
        form = HotelImageForm(request.POST, request.FILES)
        if form.is_valid():
            hotel_image_object = form.save(commit=False)
            hotel_image_object.hotel = hotel
            hotel_image_object.save()
            return redirect('update_hotel_images')
    context = {'form': form, 'hotel_images': hotel_images}
    return render(request, 'update_hotel_images.html', context)

def update_room_types(request):
    hotel_manager = HotelManager.objects.get(user=request.user)
    hotel = Hotel.objects.get(hotel_manager=hotel_manager)
    try:
        room_types = RoomType.objects.filter(hotel=hotel)
    except:
        room_types = None
    form = RoomTypeForm()
    if request.method == 'POST':
        form = RoomTypeForm(request.POST, request.FILES)
        if form.is_valid():
            room_types_object = form.save(commit=False)
            room_types_object.hotel = hotel
            room_types_object.save()
            return redirect('update_room_types')
    context = {'form': form, 'room_types': room_types}
    return render(request, 'update_room_types.html', context)

def verify(request):
    room_type = request.POST.get('room_type')
    check_in = datetime.date(datetime.strptime(request.POST.get('check_in'), '%Y-%M-%d'))
    check_out = datetime.date(datetime.strptime(request.POST.get('check_out'), '%Y-%M-%d'))

    if not(check_in and check_out and room_type):
        return HttpResponse({'kindly select all options'})
    else:
        if isRoomTypeAvailable(room_type, check_in, check_out):
            print('here')
            print(check_in)
            print(check_out)
            return HttpResponse({'room available'})
        else:
            print('there')
            return HttpResponse({'booking not available'})

def view_guest_details(request):
    curr_hotel = request.user.hotel
    # all the guests who reserved rooms in the hotel
    # all the rooms they reserved
    # all the bookings they made
    return HttpResponse("Hello")


















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
    