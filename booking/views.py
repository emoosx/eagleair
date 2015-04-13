from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import FormMixin
from django.http import HttpResponseForbidden
from flight.models import Flight
from django.db.models import Q
from models import Booking
from django import forms
from pprint import pprint
from datetime import datetime
from international.models import countries


class PurchaseForm(forms.Form):
    first_class = forms.IntegerField(required=False)
    business_class = forms.IntegerField(required=False)
    economy_class = forms.IntegerField(required=False)
    street1 = forms.CharField(required=True)
    street2 = forms.CharField(required=False)
    city = forms.CharField(required=True)
    zipcode = forms.IntegerField(required=True)
    country = forms.ChoiceField(choices=countries, required=True)




    def clean(self):
        data = super(PurchaseForm, self).clean()
        if data.get('first_class', None) or data.get('business_class', None) or data.get('economy_class', None):
            return data
        else:
            raise forms.ValidationError('Provide data for at least one field')


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


    def post(self, request, *args, **kwargs):
        if not request.user.is_authenticated():
            return HttpResponseForbidden()
        self.object = self.get_object()
        form_class = self.get_form_class()
        form = self.get_form(form_class)

        if form.is_valid():
            first_class = form.cleaned_data.get('first_class', 0)
            business_class = form.cleaned_data.get('business_class', 0)
            economy_class = form.cleaned_data.get('economy_class', 0)
            total_seats = 0

            flight = Flight.objects.get(pk=kwargs.get('pk'))
            aircraft = flight.aircraft

            if first_class > 0:
                total_seats += int(first_class)
                aircraft.seat_count_F = aircraft.seat_count_F - 1;
                aircraft.save()

            if business_class > 0:
                total_seats += int(business_class)
                aircraft.seat_count_B = aircraft.seat_count_B - 1;
                aircraft.save()

            if economy_class > 0:
                total_seats += int(economy_class)
                aircraft.seat_count_E = aircraft.seat_count_E - 1;
                aircraft.save()

            new_booking = Booking.objects.create(
                user = request.user,
                flight_id = flight,
                street1 = form.cleaned_data.get('street1'),
                street2 = form.cleaned_data.get('street2'),
                city = form.cleaned_data.get('city'),
                zipcode = form.cleaned_data.get('zipcode'),
                country = form.cleaned_data.get('country'),
                taken_seats = total_seats
            )
            new_booking.save()
            return self.form_valid(form)
        else:
            print(form.errors)
            return self.form_invalid(form)
