from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='home'),
    path('home/', views.home, name='home'),
    path('register/', views.registerCustomer, name='register'),
    path('login/', views.loginCustomer, name='login'),
    path('logout/', views.logoutCustomer, name='logout'),
    path('change_password/', views.change_password, name='change_password'),
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name="password_reset.html"),name='password_reset'), #the document says its password_reset tho
    path('password_reset_done/', auth_views.PasswordResetDoneView.as_view(template_name="password_reset_done.html"),name='password_reset_done'),
    path('password_reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="password_reset_confirm.html"),name='password_reset_confirm'),
    path('password_reset_complete/', auth_views.PasswordResetCompleteView.as_view(template_name="password_reset_complete.html"),name='password_reset_complete'),
    
] 