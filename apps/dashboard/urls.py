from django.conf.urls import patterns, url
from apps.dashboard.views import IndexView
from django.contrib.auth.decorators import login_required

urlpatterns = patterns('',
                       url(r'^$', login_required(IndexView.as_view()), name='index'),
                      )

