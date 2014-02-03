from django.conf.urls import patterns, url
from apps.gallery.views import GalleryList, GalleryCreate, GalleryRetrieve,\
    GalleryUpdate, GalleryDelete

urlpatterns = patterns('',
                       url(r'^$', GalleryList.as_view(), name='index'),
                       url(r'^create', GalleryCreate.as_view(), name='create'),
                       url(r'^(?P<slug>[-_\w]+)$', GalleryRetrieve.as_view(), name='retrieve'),
                       url(r'^(?P<slug>[-_\w]+)/update$', GalleryUpdate.as_view(), name='update'),
                       url(r'^(?P<slug>[-_\w]+)/delete$', GalleryDelete.as_view(), name='delete'),
                      )

