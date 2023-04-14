from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('home/', views.main, name='main'),
    path('gregister/', views.registerGuest, name='gregister'),
    path('glogin/', views.loginGuest, name='glogin'),
    path('glogout/', views.logoutGuest, name='glogout'),
    path('gchange_password/', views.change_password, name='gchange_password'),
    path('browse_hotels/', views.browse_hotels, name='browse_hotels'),
    path('hotel_listing/<str:pk>', views.hotel_listing, name='ghotel_listing'),
    # path('online_reservation/<str:pk>', views.online_reservation, name='online_reservation'),
]