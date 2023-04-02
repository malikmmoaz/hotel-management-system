def isRoomTypeAvailable(roomType, checkInDate, checkOutDate):
    bookings = Booking.objects.filter(room_type=roomType)
    for booking in bookings:
        if checkInDate <= booking.check_out and checkOutDate >= booking.check_in:
            return False
    return True