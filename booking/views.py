from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from flight.models import Flight


class SearchResultsView(ListView):
    template_name = 'results.html'
    context_object_name = 'available_flights'

    def get_queryset(self):
        return Flight.objects.all()

    def get_context_data(self, **kwargs):
        context = super(SearchResultsView, self).get_context_data(**kwargs)
        return context


class FlightDetailView(DetailView):
    template_name = 'flight_details.html'
