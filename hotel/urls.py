from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('hotel/', views.home, name='home'),
    path('register/', views.registerHotelManager, name='register'),
    path('login/', views.loginHotelManager, name='login'),
    path('logout/', views.logoutHotelManager, name='logout'),
    path('change_password/', views.change_password, name='change_password'),
    path('hotel_application/', views.hotel_application, name='hotel_application'),
    path('hotel_dashboard/', views.hotel_dashboard, name='hotel_dashboard'),
    path('book_room/', views.book_room, name='book_room'),
    path('update_booking/<str:pk>', views.update_booking, name='update_booking'),
    path('delete_booking/<str:pk>', views.delete_booking, name='delete_booking'),
    path('checkout/<str:pk>', views.checkout, name='checkout'),
    path('housekeeping/', views.housekeeping, name='housekeeping'),
    path('housekeeping_done/<str:pk>', views.housekeeping_done, name='housekeeping_done'),
    path('bookings/', views.bookings, name='bookings'),
    path('update_hotel_details/', views.update_hotel_details, name='update_hotel_details'),
    path('update_hotel_images/', views.update_hotel_images, name='update_hotel_images'),
    path('update_room_types/', views.update_room_types, name='update_room_types'),
    path('update_rooms/', views.update_rooms, name='update_rooms'),
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name="password_reset.html"),name='password_reset'),
    path('password_reset_done/', auth_views.PasswordResetDoneView.as_view(template_name="password_reset_done.html"),name='password_reset_done'),
    path('password_reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="password_reset_confirm.html"),name='password_reset_confirm'),
    path('password_reset_complete/', auth_views.PasswordResetCompleteView.as_view(template_name="password_reset_complete.html"),name='password_reset_complete'),
] 

htmx_urlpatterns = [
    path('verify/', views.verify, name='verify'),
]

urlpatterns += htmx_urlpatterns