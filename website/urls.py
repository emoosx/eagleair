from django.conf.urls import patterns, url, include
from django.contrib.auth.views import login, logout
from views import IndexView


urlpatterns = patterns('',
    url(r'^$', login, {'template_name': 'index.html'}, name='index'),
    url(r'^login/$', login, {'template_name': 'index.html'}, name='login'),
)
