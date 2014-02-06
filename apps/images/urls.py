from django.conf.urls import patterns, url
from apps.images.views import CreateAndListView, RetrieveAndUpdateView, DeleteView

urlpatterns = patterns('',
                       url(r'^$', CreateAndListView.as_view(), name='create_and_list'),
                       url(r'^(?P<pk>\d+)$', RetrieveAndUpdateView.as_view(), name='retrieve_and_update'),
                       url(r'^(?P<pk>\d+)/delete$', DeleteView.as_view(), name='delete'),
                      )
