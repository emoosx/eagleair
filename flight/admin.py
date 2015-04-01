from django.contrib import admin
from flight.models import *

admin.site.register(Airline)
admin.site.register(Aircraft)
admin.site.register(Airport)
admin.site.register(Flight)
