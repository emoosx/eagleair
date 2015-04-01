from django.contrib import admin
from flight.models import Airline, Airport, Country, Flight

admin.site.register(Airline)
admin.site.register(Airport)
admin.site.register(Flight)
admin.site.register(Country)
