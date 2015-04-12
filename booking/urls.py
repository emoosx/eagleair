from django.conf.urls import patterns, url
from booking.views import FlightDetailView
from flight.models import Flight

urlpatterns = patterns('',
    url(r'^flight/(?P<pk>\d+)/$', FlightDetailView.as_view(), name='flight-detail')

)
