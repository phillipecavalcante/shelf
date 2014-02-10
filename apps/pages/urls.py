from django.conf.urls import patterns, url
from apps.pages.views import *

urlpatterns = patterns('',
                       url(r'^$', IndexView.as_view(), name='index'),
#                       url(r'^basic$', ListViewBasicPage.as_view(), name='basicpage_list'),
#                       url(r'^link$', ListViewLinkPage.as_view(), name='linkpage_list'),
#                       url(r'^gallery$', ListViewGalleryPage.as_view(), name='gallerypage_list'),
#                       url(r'^basic/create$', CreateViewBasicPage.as_view(), name='basicpage_create'),
#                       url(r'^link/create$', CreateViewLinkPage.as_view(), name='linkpage_create'),
#                       url(r'^gallery/create$', CreateViewGalleryPage.as_view(), name='gallerypage_create'),
#                       url(r'^(?P<pk>\d+)$', RetrieveView.as_view(), name='retrieve'),
#                       url(r'^(?P<pk>\d+)/update$', UpdateView.as_view(), name='update'),
#                       url(r'^(?P<pk>\d+)/delete$', DeleteView.as_view(), name='delete'),
                      )