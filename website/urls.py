from django.conf.urls import patterns, url, include
from django.contrib.auth.views import login
from views import IndexView


urlpatterns = patterns('',
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^login/$', 'website.views.login_user'),
    url(r'^register/$', 'website.views.register_user'),
    url(r'^logout/$', 'website.views.logout_user'),
)
