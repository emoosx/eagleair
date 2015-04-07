from django.views.generic.edit import FormView
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render_to_response, redirect, render
from django.core.urlresolvers import reverse_lazy
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from website.forms import FrontPageSearchForm, RegistrationForm
from pprint import pprint


class IndexView(FormView):
    template_name = 'index.html'
    form_class = FrontPageSearchForm
    success_url = 'booking/search_results/'

    def get(self, *args, **kwargs):
        form = FrontPageSearchForm(self.request.GET)
        return super(IndexView, self).get(*args, **kwargs)


    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        return context

    def form_valid(self, form):
        return super(IndexView, self).form_valid(form)


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
    print 'here'
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
