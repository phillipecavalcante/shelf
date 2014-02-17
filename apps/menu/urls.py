from django.conf.urls import patterns, url
from apps.menu.views import IndexView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required

urlpatterns = patterns('',
                      url(r'^$', login_required(IndexView.as_view()), name='index'),
                      url(r'^(?P<slug>[\w-]+)$', login_required(UpdateView.as_view()), name='update'),
                      url(r'^(?P<slug>[\w-]+)/delete$', login_required(DeleteView.as_view()), name='delete'),
                      )


