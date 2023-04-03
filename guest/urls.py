from django.urls import path
from . import views

urlpatterns = [
    path('g', views.home, name='home'),
    path('ghome/', views.home, name='home'),
    path('gregister/', views.registerGuest, name='register'),
    path('glogin/', views.loginGuest, name='login'),
    path('glogout/', views.logoutGuest, name='logout'),
    path('gchange_password/', views.change_password, name='change_password'),
]