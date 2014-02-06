from django.conf.urls import patterns, url
from apps.gallery.views import CreateAndListView, GalleryDelete, CreateAndListImageView

urlpatterns = patterns('',
                       url(r'^$', CreateAndListView.as_view(), name='create_and_list'),
                       url(r'^(?P<slug>[-_\w]+)$', CreateAndListImageView.as_view(), name='create_and_list_images'),
                       url(r'^(?P<slug>[-_\w]+)/delete$', GalleryDelete.as_view(), name='delete'),
                      )

