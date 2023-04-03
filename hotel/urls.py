from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('home/', views.home, name='home'),
    path('register/', views.registerHotelManager, name='register'),
    path('login/', views.loginHotelManager, name='login'),
    path('logout/', views.logoutHotelManager, name='logout'),
    path('change_password/', views.change_password, name='change_password'),
    path('hotel_application/', views.hotel_application, name='hotel_application'),
] 