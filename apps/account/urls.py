from django.conf.urls import patterns, url
from apps.account.views import logout_view

urlpatterns = patterns('',
                      url(r'^$', logout_view, name='index'),
                      )