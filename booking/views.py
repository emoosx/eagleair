from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import FormMixin
from flight.models import Flight
from django.db.models import Q
from django import forms
from pprint import pprint
from datetime import datetime


class PurchaseForm(forms.Form):
    first_class = forms.IntegerField(required=True)
    business_class = forms.IntegerField(required=True)
    economy_class = forms.IntegerField(required=True)


class FlightDetailView(FormMixin, DetailView):
    model = Flight
    context_object_name = 'flight'
    template_name = 'flight_details.html'
    form_class = PurchaseForm
    success_url = '.'

    def get_context_data(self, **kwargs):
        context = super(FlightDetailView, self).get_context_data(**kwargs)
        form_class = self.get_form_class()
        context['form'] = self.get_form(form_class)
        return context

    def form_valid(self, form):
        return super(FlightDetailView, self).form_valid(form)
