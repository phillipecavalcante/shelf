#===============================================================================
# DJANGO
#===============================================================================
from django.conf.urls import patterns, url, include
#===============================================================================
# IMAGES
#===============================================================================
from apps.images.views import IndexView, DeleteView, UpdateView

urlpatterns = patterns('',
                       #========================================================
                       # IMAGES
                       #========================================================
                       url(r'^a$', IndexView.as_view(), name='index'),
                       url(r'^(?P<slug>[\w-]+)$', UpdateView.as_view(), name='update'),
                       url(r'^(?P<slug>[\w-]+)/delete$', DeleteView.as_view(), name='delete'),
                       url(r'^', include('haystack.urls'), name='search'),
                      )
