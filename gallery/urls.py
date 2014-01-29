from django.conf.urls import patterns, url
from gallery.views import GalleryList, GalleryCreate

urlpatterns = patterns('',
                      url(r'^$', GalleryList.as_view(), name='list'),
                      url(r'^create$', GalleryCreate.as_view(), name='create'),
#                       url(r'^(?P<pk>\d+)$', Retrieve.as_view(), name='retrieve'),
#                       url(r'^(?P<pk>\d+)/update$', UpdateView.as_view(), name='update'),
#                       url(r'^(?P<pk>\d+)/delete$', DeleteView.as_view(), name='delete'),
                      )

