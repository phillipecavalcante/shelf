from django.conf.urls import patterns, url
from django.contrib.auth.decorators import login_required
from apps.gallery.views import IndexView, UpdateView, DeleteView
 
urlpatterns = patterns('',
                       url(r'^$', login_required(IndexView.as_view()), name='index'),
                       url(r'^(?P<slug>[\w-]+)$', login_required(UpdateView.as_view()), name='update'),
                       url(r'^(?P<slug>[\w-]+)/delete$', login_required(DeleteView.as_view()), name='delete'),
                       url(r'^search/', login_required('apps.gallery.views.search_names') , name='search'),
                      )

