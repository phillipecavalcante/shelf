from django.conf.urls import patterns, url
from website.views import IndexView, DetailView

urlpatterns = patterns('',
                      url(r'^$', IndexView.as_view(), name='index'),
                      url(r'^page/(?P<pk>\d+)$', DetailView.as_view(), name='page'),
                      )