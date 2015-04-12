from django.contrib import admin
from booking.models import Booking

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('flight_id', 'user', 'taken_seats', 'created_at')
