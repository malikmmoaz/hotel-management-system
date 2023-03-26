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


# Create your views here.
def home(request):
    return render(request, 'home.html')

def registerCustomer(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
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
            form.save()
            messages.success(request, 'Account was created successfully')
            return redirect('login')
    context = {'form': form}
    return render(request, 'register.html', context)

def loginCustomer(request):
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

def logoutCustomer(request):
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

def hotel_application(request):
    form = HotelApplicationForm()
    if request.method == 'POST':
        form = HotelApplicationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your application was successfully submitted!')
            return redirect('home')
    context = {'form': form}
    return render(request, 'hotel_application.html', context)