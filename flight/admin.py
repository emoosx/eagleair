from django.contrib import admin
from flight.models import *
from eagleair.admin import user_admin_site


# @admin.register(Airline)
class AirlineAdmin(admin.ModelAdmin):
    list_display = ('name', 'country', 'iata_code')

admin.site.register(Airline, AirlineAdmin)
user_admin_site.register(Airline, AirlineAdmin)


# @admin.register(Airport)
class AirportAdmin(admin.ModelAdmin):
    list_display = ('name', 'city', 'country', 'iata_code')

admin.site.register(Airport, AirportAdmin)
user_admin_site.register(Airport, AirportAdmin)


# @admin.register(Aircraft)
class AircraftAdmin(admin.ModelAdmin):
    list_display = ('model', 'seat_count_F', 'seat_count_B', 'seat_count_E')

admin.site.register(Aircraft, AircraftAdmin)
user_admin_site.register(Aircraft, AircraftAdmin)


# @admin.register(Flight)
class FlightAdmin(admin.ModelAdmin):
    list_display = ('code', 'from_airport', 'departure_date', 'departure_time',
                    'to_airport', 'arrival_date', 'arrival_time')

admin.site.register(Flight, FlightAdmin)
user_admin_site.register(Flight, FlightAdmin)
