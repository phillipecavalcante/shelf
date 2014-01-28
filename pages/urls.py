from django.conf.urls import patterns, url
from pages.views import IndexView, CreateView, RetrieveView, UpdateView, DeleteView

urlpatterns = patterns('',
                      url(r'^$', IndexView.as_view(), name='index'),
                      url(r'^create$', CreateView.as_view(), name='create'),
                      url(r'^(?P<pk>\d+)$', RetrieveView.as_view(), name='retrieve'),
                      url(r'^(?P<pk>\d+)/update$', UpdateView.as_view(), name='update'),
                      url(r'^(?P<pk>\d+)/delete$', DeleteView.as_view(), name='delete'),
                      )