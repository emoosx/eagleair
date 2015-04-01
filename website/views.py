from django.contrib.auth import logout, login
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        return context


def logout_page(request):
    logout(request)
    return HttpResponseRedirect('/')
