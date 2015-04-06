from django.contrib import admin
from flight.models import *


@admin.register(Airline)
class AirlineAdmin(admin.ModelAdmin):
    list_display = ('name', 'country', 'iata_code')


@admin.register(Airport)
class AirportAdmin(admin.ModelAdmin):
    list_display = ('name', 'city', 'country', 'iata_code')


@admin.register(Aircraft)
class AircraftAdmin(admin.ModelAdmin):
    list_display = ('model', 'seat_count_F', 'seat_count_B', 'seat_count_E')


@admin.register(Flight)
class FlightAdmin(admin.ModelAdmin):
    list_display = ('code', 'from_airport', 'departure_date', 'departure_time',
                    'to_airport', 'arrival_date', 'arrival_time')
