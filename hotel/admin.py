from django.contrib import admin
from .models import *

admin.site.register(HotelManager)
admin.site.register(HotelApplication)
admin.site.register(Hotel)
admin.site.register(HotelImage)
admin.site.register(RoomType)
admin.site.register(Room)
admin.site.register(HotelBooking)