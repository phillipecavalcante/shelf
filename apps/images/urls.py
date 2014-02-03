from django.conf.urls import patterns, url
from apps.images.views import ListView, CreateView, RetrieveView, UpdateView,\
    DeleteView

urlpatterns = patterns('',
                       url(r'^$', ListView.as_view(), name='list'),
                       url(r'^create', CreateView.as_view(), name='create'),
                       url(r'^(?P<pk>\d+)$', RetrieveView.as_view(), name='retrieve'),
                       url(r'^(?P<pk>\d+)/update$', UpdateView.as_view(), name='update'),
                       url(r'^(?P<pk>\d+)/delete$', DeleteView.as_view(), name='delete'),
                      )
