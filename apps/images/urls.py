from django.conf.urls import patterns, url
from apps.images.views import CreateAndListView, RetrieveView, UpdateView,\
    DeleteView

urlpatterns = patterns('',
                       url(r'^$', CreateAndListView.as_view(), name='create_and_list'),
                       url(r'^(?P<pk>\d+)$', RetrieveView.as_view(), name='retrieve'),
                       url(r'^(?P<pk>\d+)/update$', UpdateView.as_view(), name='update'),
                       url(r'^(?P<pk>\d+)/delete$', DeleteView.as_view(), name='delete'),
                      )
