#===============================================================================
# DJANGO
#===============================================================================
from django.conf.urls import patterns, url
#===============================================================================
# PAGES
#===============================================================================
from apps.pages.views import *
from django.contrib.auth.decorators import login_required
#===============================================================================
# URL PATTERNS
#===============================================================================
urlpatterns = patterns('',
                        url(r'^$', login_required(PageIndexView.as_view()), name='index'),
                        url(r'^(?P<slug>[\w-]+)$', login_required(PageUpdateView.as_view()), name='update'),
                        url(r'^(?P<slug>[\w-]+)/delete$', login_required(PageDeleteView.as_view()), name='delete'),
                        url(r'^search/', 'apps.pages.views.search_pages' , name='search'),
                      )