from django.core.urlresolvers import reverse_lazy
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.db.models import Q, F
from django.views.generic.edit import FormView
from django.contrib.auth.models import User
from django.contrib.auth import logout, login, authenticate
from flight.models import Flight, Aircraft
from django.shortcuts import redirect, render_to_response, render
from website.forms import FrontPageSearchForm, RegistrationForm
from pprint import pprint
from datetime import datetime

DATE_FORMAT = "%d %B, %Y"

class IndexView(FormView):
    template_name = 'index.html'
    form_class = FrontPageSearchForm
    success_url = '.'

    def get(self, *args, **kwargs):
        if self.request.GET:
            form = FrontPageSearchForm(data=self.request.GET)
            if form.is_valid():
                _no_of_guests = self.request.GET.get('no_of_guests')
                _trip_type = self.request.GET.get('trip_type')
                _departure = self.request.GET.get('departure')
                _departure_date = self.request.GET.get('departure_date')
                _departure_date = datetime.strptime(_departure_date, DATE_FORMAT).date()
                _arrival = self.request.GET.get('arrival')
                _arrival_date = self.request.GET.get('arrival_date', None)

                aircrafts = Aircraft.objects.filter(
                    seat_count_F__gte=_no_of_guests-F('seat_count_B')-F('seat_count_E')
                )
                available_flights = Flight.objects.filter(
                    Q(from_airport__iata_code=_departure) &
                    Q(to_airport__iata_code=_arrival) &
                    Q(departure_date=_departure_date) &
                    Q(aircraft__in=aircrafts)
                    # Q(aircraft__seats__gte=_no_of_guests)
                )
                if _trip_type != "one":
                    if _arrival_date:
                        _arrival_date = datetime.strptime(_arrival_date, DATE_FORMAT).date()
                        available_flights = available_flights.filter(
                            Q(arrival_date = _arrival_date)
                        )


                return self.render_to_response(self.get_context_data(form=form, available_flights=available_flights))

            else: # form is invalid
                return self.render_to_response(self.get_context_data(form=form))
        return super(IndexView, self).get(*args, **kwargs)



def login_user(request):
    logout(request)
    username = password = ''
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('website:index')
    return render_to_response('login.html', context_instance=RequestContext(request))


def logout_user(request):
    logout(request)
    return redirect('website:index')


def register_user(request):
    registered = False
    if request.POST:

        registration_form = RegistrationForm(data=request.POST)

        if registration_form.is_valid():
            user = registration_form.save()
            user.set_password(user.password)
            user.save()
            registered = True
            return render(request,
                          'login.html',
                          {'registration_form': registration_form,
                           'registered': registered})
        else:
            print registration_form.errors
            return render(request,
                          'login.html',
                          {'registration_form': registration_form,
                           'registered': registered})

    else:
        registration_form = RegistrationForm()

    return render(request,
                  'login.html',
                  {'registration_form': registration_form,
                   'registered': registered})
