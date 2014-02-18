from django.conf.urls import patterns, url
from apps.website.views import IndexView, PageDetailView

urlpatterns = patterns('',
                      url(r'^$', IndexView.as_view(), name='index'),
                      url(r'^(?P<slug>[\w-]+)$', PageDetailView.as_view(), name='retrieve'),
                      url(r'^p/(?P<slug>[\w-]+)$', 'apps.website.views.dados' , name='dados'),
                      )