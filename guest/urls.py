from django.urls import path
from . import views

urlpatterns = [
    path('g', views.home, name='ghome'),
    path('ghome/', views.home, name='ghome'),
    path('gregister/', views.registerGuest, name='gregister'),
    path('glogin/', views.loginGuest, name='glogin'),
    path('glogout/', views.logoutGuest, name='glogout'),
    path('gchange_password/', views.change_password, name='gchange_password'),
    path('hotel_listing/', views.hotel_listing, name='ghotel_listing'),
]