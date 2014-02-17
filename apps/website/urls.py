from django.conf.urls import patterns, url
from apps.website.views import IndexView, TextPageDetailView

urlpatterns = patterns('',
                      url(r'^$', IndexView.as_view(), name='index'),
                      url(r'^tp/(?P<slug>[\w-]+)$', TextPageDetailView.as_view(), name='textpage_retrieve'),
                      )