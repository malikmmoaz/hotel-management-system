from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(HotelApplication)

admin.site.register(Hotel)

admin.site.register(HotelImage)

admin.site.register(RoomType)

admin.site.register(Room)

admin.site.register(HotelManager)

