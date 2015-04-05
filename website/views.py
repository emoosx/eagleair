from django.views.generic import FormView
from forms import FrontPageSearchForm


class IndexView(FormView):
    template_name = 'index.html'
    form_class = FrontPageSearchForm
    success_url = '.'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        return context

    def form_valid(self, form):
        return super(IndexView, self).form_valid(form)

