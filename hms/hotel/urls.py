from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('home/', views.home, name='home'),
    path('register/', views.registerCustomer, name='register'),
    path('login/', views.loginCustomer, name='login'),
    path('logout/', views.logoutCustomer, name='logout'),
] 