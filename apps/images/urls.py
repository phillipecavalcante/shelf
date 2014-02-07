from django.conf.urls import patterns, url
from apps.images.views import IndexView, RetrieveAndUpdateView, DeleteView

urlpatterns = patterns('',
                       url(r'^$', IndexView.as_view(), name='index'),
                       url(r'^(?P<pk>\d+)$', RetrieveAndUpdateView.as_view(), name='retrieve_and_update'),
                       url(r'^(?P<pk>\d+)/delete$', DeleteView.as_view(), name='delete'),
                      )
