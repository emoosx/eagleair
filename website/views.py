from django.views.generic.edit import FormView
from website.forms import FrontPageSearchForm
from flight.models import Flight
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
