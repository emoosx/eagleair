from django.conf.urls import patterns, include, url
from django.contrib import admin
from admin import user_admin_site

urlpatterns = patterns('',
    url(r'^', include('website.urls', namespace='website')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^flight/', include('flight.urls', namespace='flight')),
    url(r'^booking/', include('booking.urls', namespace='booking')),
)
