from django.conf.urls import patterns, url
from apps.gallery.views import GalleryList, GalleryCreate, GalleryRetrieve,\
    GalleryUpdate, GalleryDelete, ImageCreateView

urlpatterns = patterns('',
                       url(r'^$', GalleryList.as_view(), name='index'),
                       url(r'^create', GalleryCreate.as_view(), name='create'),
                       url(r'^(?P<pk>\d+)$', GalleryRetrieve.as_view(), name='retrieve'),
                       url(r'^(?P<pk>\d+)/update$', GalleryUpdate.as_view(), name='update'),
                       url(r'^(?P<pk>\d+)/delete$', GalleryDelete.as_view(), name='delete'),
                       url(r'^image/create', ImageCreateView.as_view(), name='image_create'),
#                        url(r'^gallery/(?P<pk>\d+)$', GalleryRetrieveView.as_view(), name='gretrieve'),
#                       url(r'^(?P<pk>\d+)$', Retrieve.as_view(), name='retrieve'),
#                       url(r'^(?P<pk>\d+)/update$', UpdateView.as_view(), name='update'),
#                       url(r'^(?P<pk>\d+)/delete$', DeleteView.as_view(), name='delete'),
                      )

