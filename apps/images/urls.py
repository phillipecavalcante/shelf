from django.conf.urls import patterns, url
from apps.images.views import IndexView, DeleteView, UpdateView

urlpatterns = patterns('',
                        url(r'^$', IndexView.as_view(), name='index'),
                        url(r'^(?P<slug>[\w-]+)$', UpdateView.as_view(), name='update'),
                        url(r'^(?P<slug>[\w-]+)/delete$', DeleteView.as_view(), name='delete'),
                      )
