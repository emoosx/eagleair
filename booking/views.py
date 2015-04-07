from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from flight.models import Flight
from django.db.models import Q
from pprint import pprint
from datetime import datetime


class SearchResultsView(ListView):
    template_name = 'results.html'
    context_object_name = 'available_flights'

    def get_queryset(self):

        DATE_FORMAT = "%d %B, %Y"
        _no_of_guests = self.request.GET.get('no_of_guests')
        _trip_type = self.request.GET.get('trip_type')
        _departure = self.request.GET.get('departure')
        _departure_date = self.request.GET.get('departure_date')
        _departure_date = datetime.strptime(_departure_date, DATE_FORMAT).date()
        _arrival = self.request.GET.get('arrival')
        _arrival_date = self.request.GET.get('arrival_date', '')

        print _departure_date


        available_flights = Flight.objects.filter(
            Q(from_airport__iata_code = _departure) &
            Q(to_airport__iata_code = _arrival) &
            Q(departure_date = _departure_date)
        )

        if _trip_type != "one":
            if _arrival_date:
                _arrival_date = datetime.strptime(_arrival_date, DATE_FORMAT).date()
                available_flights = available_flights.filter(
                    Q(arrival_date = _arrival_date)
                )

        return available_flights

    def get_context_data(self, **kwargs):
        context = super(SearchResultsView, self).get_context_data(**kwargs)
        return context


class FlightDetailView(DetailView):
    template_name = 'flight_details.html'
