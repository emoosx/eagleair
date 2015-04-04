from django.conf.urls import patterns, url, include
from django.contrib.auth.views import login
from views import IndexView


urlpatterns = patterns('',
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^login/$', login, {'template_name': 'login.html'}, name='login'),
)
