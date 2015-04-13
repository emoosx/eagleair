from django.contrib import admin
from eagleair.admin import user_admin_site
from booking.models import Booking


# @user_admin_site.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('flight_id', 'user', 'taken_seats', 'created_at')

admin.site.register(Booking, BookingAdmin)
user_admin_site.register(Booking, BookingAdmin)
