from django.conf.urls import patterns, url
from gallery.views import ImageCreateView, ImageRetrieveView, CreateGallery,\
    GalleryRetrieveView

urlpatterns = patterns('',
                      url(r'^create', CreateGallery.as_view(), name='gallery_create'),
                      url(r'^(?P<pk>\d+)$', ImageRetrieveView.as_view(), name='retrieve'),
                      url(r'^image/create', ImageCreateView.as_view(), name='image_create'),
                      url(r'^gallery/(?P<pk>\d+)$', GalleryRetrieveView.as_view(), name='gretrieve'),
#                       url(r'^(?P<pk>\d+)$', Retrieve.as_view(), name='retrieve'),
#                       url(r'^(?P<pk>\d+)/update$', UpdateView.as_view(), name='update'),
#                       url(r'^(?P<pk>\d+)/delete$', DeleteView.as_view(), name='delete'),
                      )

