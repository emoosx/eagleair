from django.shortcuts import render
from django.views.generic import FormView
from website.forms import RegistrationForm

# Create your views here.
class CreateUser(FormView):
    template_name = 'register.html'
    success_url = '.'
    form_class = RegistrationForm

    def form_valid(self, form):
        user = User.objects.create_user(
            username=form.cleaned_data['username'],
            password=form.cleaned_data['password'],
            email=form.cleaned_data['email']
        )
        return super(CreateUser, self).form_valid(form)
