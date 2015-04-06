from django.conf.urls import patterns, url
from booking.views import SearchResultsView

urlpatterns = patterns('',
    url(r'^search_results/$', SearchResultsView.as_view(), name='search_results'),
)
