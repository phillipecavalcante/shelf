#===============================================================================
# DJANGO
#===============================================================================
from django.conf.urls import patterns, url
from django.contrib.auth.decorators import login_required
#===============================================================================
# PAGES
#===============================================================================
from apps.pages.views import *
#===============================================================================
# URL PATTERNS
#===============================================================================
urlpatterns = patterns('',
                       url(r'^$', IndexView.as_view(), name='index'),
                       #========================================================
                       # LINK PAGE
                       #========================================================
                       url(r'^linkpages$', login_required(LinkPageIndexView.as_view()), name='linkpage_index'),
                       url(r'^linkpages/(?P<slug>[\w-]+)$', LinkPageUpdateView.as_view(), name='linkpage_update'),
                       url(r'^linkpages/(?P<slug>[\w-]+)/delete$', LinkPageDeleteView.as_view(), name='linkpage_delete'),
                       #========================================================
                       # TEXT PAGE
                       #========================================================
                       url(r'^textpages$', TextPageIndexView.as_view(), name='textpage_index'),
                       url(r'^textpages/(?P<slug>[\w-]+)$', TextPageUpdateView.as_view(), name='textpage_update'),
                       url(r'^textpages/(?P<slug>[\w-]+)/delete$', TextPageDeleteView.as_view(), name='textpage_delete'),
                       #========================================================
                       # GALLERY PAGE
                       #========================================================
                       url(r'^gallerypages$', GalleryPageIndexView.as_view(), name='gallerypage_index'),
                       url(r'^gallerypages/(?P<slug>[\w-]+)$', GalleryPageUpdateView.as_view(), name='gallerypage_update'),
                       url(r'^gallerypages/(?P<slug>[\w-]+)/delete$', GalleryPageDeleteView.as_view(), name='gallerypage_delete'),
                       #========================================================
                       # PRODUCT PAGE
                       #========================================================
                       url(r'^productpages$', ProductPageIndexView.as_view(), name='productpage_index'),
                       url(r'^productpages/(?P<slug>[\w-]+)$', ProductPageUpdateView.as_view(), name='productpage_update'),
                       url(r'^productpages/(?P<slug>[\w-]+)/delete$', ProductPageDeleteView.as_view(), name='productpage_delete'),
                      )