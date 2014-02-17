#===============================================================================
# DJANGO
#===============================================================================
from django.conf.urls import patterns, url, include
#===============================================================================
# IMAGES
#===============================================================================
from apps.images.views import IndexView, DeleteView, UpdateView
from django.contrib.auth.decorators import login_required

urlpatterns = patterns('',
                       #========================================================
                       # IMAGES
                       #========================================================
                       url(r'^$', login_required(IndexView.as_view()), name='index'),
                       url(r'^(?P<slug>[\w-]+)$', login_required(UpdateView.as_view()), name='update'),
                       url(r'^(?P<slug>[\w-]+)/delete$', login_required(DeleteView.as_view()), name='delete'),
                       url(r'^search/', 'apps.images.views.search_names' , name='search'),
                      )
